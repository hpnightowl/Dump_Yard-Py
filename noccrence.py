n=int(input())
lst=list()
for i in  range(0,n):
    temp=int(input())
    lst.append(temp)
print(list(set(lst)))