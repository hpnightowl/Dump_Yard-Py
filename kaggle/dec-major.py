import pandas as pd

def di():
    for i in range(0, 50):
        print("*",end='')
    print("\n")def di():
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
