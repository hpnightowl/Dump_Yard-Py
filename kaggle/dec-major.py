import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def di():
    for i in range(0, 50):
        print("*",end='')
    print("\n")

dt_test = pd.read_excel("Data_Test.xlsx")
dt_train = pd.read_excel("Data_Train.xlsx")
#backupdata
df_train_orig = dt_train.copy()
df_test_orig = dt_test.copy()

di()
print(dt_test)
print(dt_train)
di()
#columns
print(dt_train.columns)
print(dt_test.columns)
di()
#heads
print(dt_train.head())
print(dt_test.head())
di()
#info
dt_test.info()
di()
#describe
print(dt_train.describe())
print(dt_test.describe())
di()
#finding nulls
print(pd.isnull(dt_test).sum())
print(pd.isnull(dt_train).sum())
di()
print(dt_train.shape)
print(dt_test.shape)


df_train_orig = dt_train.copy()
df_test_orig = dt_test.copy()


print("Skew ", dt_train['Price'].skew())
print("kurt ", dt_train['Price'].kurt())

df_test1 = np.log1p(dt_train['Price'].values)

df_test1 = df_test1.reshape(-1,1)
df_test1 = pd.DataFrame(df_test1, columns=['PriceNew'])

di()
print("Skew ", df_test1['PriceNew'].skew())
print("kurt ", df_test1['PriceNew'].kurt())

di()
print(dt_train.head())
di()
print(dt_test.sample(5))

di()
print(dt_train.shape)
print(dt_test.shape)
di()
print(dt_train.describe())
di()

#finding missing data
missed = (dt_train.isnull().sum() / len(dt_train))
missing = pd.DataFrame({"Missing":missed, 'count':dt_train.isnull().sum()}).sort_values(by="Missing", ascending=False)
print(missing)
missing.loc[missing['Missing'] > 0]
missed = (dt_test.isnull().sum() / len(dt_test))
missing = pd.DataFrame({"Missing":missed, 'count':dt_test.isnull().sum()}).sort_values(by="Missing", ascending=False)
missing.loc[missing['Missing'] > 0]
print(missing)
di()

g2 = sns.countplot(x='Fuel_Type', data=dt_train)
loc,labels = plt.xticks()
#the above graph shows that the Diesel Cars Are more in demand

plt.show()
#change the name block to company name though we have original data present

dt_train['Name'] = dt_train['Name'].apply(lambda x: str(x).split(" ")[0])
dt_test['Name'] = dt_test['Name'].apply(lambda x: str(x).split(" ")[0])

print(dt_test.head(5))


import re

dt_train['Mileage_upd'] = dt_train['Mileage'].apply(lambda x: re.sub(r'(\d+\.\d+)\s(kmpl|km\/kg)', r'\1', str(x)))
dt_train['Engine_upd'] = dt_train['Engine'].apply(lambda x: re.sub(r'(\d+)\s(CC)', r'\1', str(x)))
dt_train['Power_upd'] = dt_train['Power'].apply(lambda x: re.sub(r'(\d+\.?\d+?)\s(bhp)', r'\1', str(x)))

dt_test['Mileage_upd'] = dt_test['Mileage'].apply(lambda x: re.sub(r'(\d+\.\d+)\s(kmpl|km\/kg)', r'\1', str(x)))
dt_test['Engine_upd'] = dt_test['Engine'].apply(lambda x: re.sub(r'(\d+)\s(CC)', r'\1', str(x)))
dt_test['Power_upd'] = dt_test['Power'].apply(lambda x: re.sub(r'(\d+\.?\d+?)\s(bhp)', r'\1', str(x)))

dt_train['Mileage_upd'] = pd.to_numeric(dt_train['Mileage_upd'], errors='coerce')
dt_train['Engine_upd'] = pd.to_numeric(dt_train['Engine_upd'], errors='coerce')
dt_train['Power_upd'] = pd.to_numeric(dt_train['Power_upd'], errors='coerce')

dt_test['Mileage_upd'] = pd.to_numeric(dt_test['Mileage_upd'], errors='coerce')
dt_test['Engine_upd'] = pd.to_numeric(dt_test['Engine_upd'], errors='coerce')
dt_test['Power_upd'] = pd.to_numeric(dt_test['Power_upd'], errors='coerce')

dt_train.drop(columns=['Mileage', 'Engine', 'Power'], inplace=True)
dt_test.drop(columns=['Mileage', 'Engine', 'Power'], inplace=True)

dt_train.drop(dt_train[dt_train['Name'] == 'Smart'].index, axis=0, inplace=True)
dt_test.drop(dt_test[dt_test['Name'] == 'Hindustan'].index, axis=0, inplace=True)


#Function to replace na value with mode of that specific brand
def fill_na_with_mode(ds, Name, colname):
  fill_value = ds.loc[ds['Name'] == Name][colname].mode()[0]
  condit = ((ds['Name'] == Name) & (ds[colname].isnull()))
  ds.loc[condit, colname] = ds.loc[condit, colname].fillna(fill_value)


uqe_mil = dt_train.loc[dt_train['Mileage_upd'].isnull()]['Name'].unique()
uqe_eng = dt_train.loc[dt_train['Engine_upd'].isnull()]['Name'].unique()
miss_Power_col = dt_train.loc[dt_train['Power_upd'].isnull()]['Name'].unique()

for x in uqe_mil:
  fill_na_with_mode(dt_train, x, 'Mileage_upd')
for y in uqe_eng:
  fill_na_with_mode(dt_train, y, 'Engine_upd')
for z in miss_Power_col:
  fill_na_with_mode(dt_train, z, 'Power_upd')


miss_ts_Mileage_col = dt_test.loc[dt_test['Mileage_upd'].isnull()]['Name'].unique()
miss_ts_Engine_col = dt_test.loc[dt_test['Engine_upd'].isnull()]['Name'].unique()
miss_ts_Power_col = dt_test.loc[dt_test['Power_upd'].isnull()]['Name'].unique()

for x in miss_ts_Mileage_col:
  fill_na_with_mode(dt_test, x, 'Mileage_upd')
for y in miss_ts_Engine_col:
  fill_na_with_mode(dt_test, y, 'Engine_upd')
for z in miss_ts_Power_col:
  fill_na_with_mode(dt_test, z, 'Power_upd')

zero_mileage_col = dt_train.loc[dt_train['Mileage_upd'] == 0.0]['Name'].unique()

for m in zero_mileage_col:
  fill_zero = dt_train.loc[dt_train['Name'] == m]['Mileage_upd'].mode()[0]
  m1 = ((dt_train['Name'] == m) & (dt_train['Mileage_upd'] == 0.0))
  dt_train.loc[m1, 'Mileage_upd'] = fill_zero

zero_mileage_col2 = dt_test.loc[dt_test['Mileage_upd'] == 0.0]['Name'].unique()
#df_train.loc[df_train['brand_name'] == 'Maruti']['Seats'].mode()[0]
def fill_na_with_mode(ds, Name):
  fill_value = ds.loc[ds['Name'] == Name]['Seats'].mode()[0]
  condit = ((ds['Name'] == Name) & (ds['Seats'].isnull()))
  ds.loc[condit, 'Seats'] = ds.loc[condit, 'Seats'].fillna(fill_value)


car_brand = ['Maruti','Hyundai','BMW','Fiat','Land','Ford','Toyota','Honda','Skoda','Mahindra']
for c in car_brand:
  fill_na_with_mode(dt_train, c)
  fill_na_with_mode(dt_test, c)
for m in zero_mileage_col2:
  fill_zero = dt_test.loc[dt_test['Name'] == m]['Mileage_upd'].mode()[0]
  m1 = ((dt_test['Name'] == m) & (dt_test['Mileage_upd'] == 0.0))
  dt_test.loc[m1, 'Mileage_upd'] = fill_zero


m1 = (dt_train['Seats'] == 0.0)
dt_train.loc[m1, 'Seats'] = 5.0


plt.figure(figsize=(20,8))
plt.subplot(1,2,1)
sns.distplot(dt_train['Price'])

plt.subplot(1,2,2)
sns.boxplot(y=dt_train['Price'])
plt.show()


fig = plt.figure(figsize=(20,18))
fig.subplots_adjust(hspace=0.2, wspace=0.2)
fig.add_subplot(2,2,1)
g1 = sns.countplot(x='Name', data=dt_train)
loc,labels = plt.xticks()
g1.set_xticklabels(labels,rotation=90)

g2.set_xticklabels(labels,rotation=0)
fig.add_subplot(2,2,3)
g3 = sns.countplot(x='Transmission', data=dt_train)
loc,labels = plt.xticks()
g3.set_xticklabels(labels,rotation=0)
fig.add_subplot(2,2,4)
g4 = sns.countplot(x='Owner_Type', data=dt_train)
loc,labels = plt.xticks()
g4.set_xticklabels(labels,rotation=0)
plt.show()


fig = plt.figure(figsize=(15,15))
fig.subplots_adjust(hspace=0.2, wspace=0.2)
ax1 = fig.add_subplot(2,2,1)
plt.xlim([0, 100000])
p1 = sns.scatterplot(x="Kilometers_Driven", y="Price", data=dt_train)
loc, labels = plt.xticks()
ax1.set_xlabel('Kilometer')

ax2 = fig.add_subplot(2,2,2)
#plt.xlim([0, 100000])
p2 = sns.scatterplot(x="Mileage_upd", y="Price", data=dt_train)
loc, labels = plt.xticks()
ax2.set_xlabel('Mileage')

ax3 = fig.add_subplot(2,2,3)
#plt.xlim([0, 100000])
p3 = sns.scatterplot(x="Engine_upd", y="Price", data=dt_train)
loc, labels = plt.xticks()
ax3.set_xlabel('Engine')

ax4 = fig.add_subplot(2,2,4)
#plt.xlim([0, 100000])
p4 = sns.scatterplot(x="Power_upd", y="Price", data=dt_train)
loc, labels = plt.xticks()
ax4.set_xlabel('Power')

plt.show()


fig = plt.figure(figsize=(18,5))
fig.subplots_adjust(hspace=0.3, wspace=0.3)

ax1 = fig.add_subplot(1,2,1)
sns.scatterplot(x='Price', y="Year", data=dt_train)
ax1.set_xlabel('Price')
ax1.set_ylabel('Year')
ax1.set_title('Year vs Price')

ax2 = fig.add_subplot(1,2,2)
sns.scatterplot(x='Price', y='Kilometers_Driven', data=dt_train)
ax2.set_ylabel('kilometer')
ax2.set_xlabel('Price')
ax2.set_title('Kilometer vs Price')
plt.show()

dt_train.drop(dt_train[dt_train['Kilometers_Driven'] >= 6500000].index, axis=0, inplace=True)

df_vis_1 = pd.DataFrame(dt_train.groupby('Name')['Price'].mean())
df_vis_1.plot.bar()
plt.show()

fig = plt.figure(figsize=(20,8))
ax1 = fig.add_subplot(1,2,1)
sns.boxplot(x='Owner_Type', y='Price', data=dt_train)
ax1.set_title('Owner vs Price')

ax2 = fig.add_subplot(1,2,2)
sns.boxplot(x='Name', y='Price', data=dt_train)
loc,labels = plt.xticks()
ax2.set_xticklabels(labels, rotation=90)
ax2.set_title('Brand vs Price')
plt.show()


fig = plt.figure(figsize=(18,6))
ax1 = fig.add_subplot(1,3,1)
sns.boxplot(x='Seats', y='Price', data=dt_train)
ax1.set_title('Seats vs Price')

ax2 = fig.add_subplot(1,3,2)
sns.boxplot(x='Transmission', y='Price', data=dt_train)
ax2.set_title('Transmission vs Price')

ax3 = fig.add_subplot(1,3,3)
sns.boxplot(x='Fuel_Type', y='Price', data=dt_train)
ax3.set_title('Fuel vs Price')

plt.show()


import datetime
now = datetime.datetime.now()
dt_train['Year_upd'] = dt_train['Year'].apply(lambda x : now.year - x)
dt_test['Year_upd'] = dt_test['Year'].apply(lambda x : now.year - x)



dt_train.drop(columns=['Year'], axis=1, inplace=True)
dt_test.drop(columns=['Year'], axis=1, inplace=True)

#drop the price
dt_train.drop(columns=['New_Price'], axis=1, inplace=True)
dt_test.drop(columns=['New_Price'], axis=1, inplace=True)


#remove location based price prediction

dt_train.drop(columns=['Location'], axis=1, inplace=True)
dt_test.drop(columns=['Location'], axis=1, inplace=True)
df_train_norm = pd.get_dummies(dt_train, drop_first=True)
df_test_norm = pd.get_dummies(dt_test, drop_first=True)


#conversion of data for manupilation

df_train_norm['Price_upd'] = np.log1p(df_train_norm['Price'].values)

#1. add new column after taking logarithm for the dependent variable to avoid high skewness & kurtosis


df_train_norm.drop(columns=['Price'], axis=1, inplace=True)


df_train_X = df_train_norm.drop(columns=['Price_upd'], axis=1)
df_train_y = df_train_norm[['Price_upd']]

# Seperated X & y values

df_train_X = (df_train_X - df_train_X.mean())/df_train_X.std()
df_test_norm = (df_test_norm - df_test_norm.mean())/df_test_norm.std()

#1. Normalized the train and test data


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(df_train_X, df_train_y, test_size=0.1, random_state=1)
reg = lm.fit(X_train, y_train)
print(reg)

#verify accuracy

y_predict = reg.predict(X_test)
print(y_predict)

from sklearn.metrics import r2_score

r2_score(y_predict, y_test)

print("Accuracy(in Percentage)-",reg.score(X_test,y_test)*100)
