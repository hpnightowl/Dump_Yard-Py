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
