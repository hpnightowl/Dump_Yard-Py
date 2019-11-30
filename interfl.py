n=int(input())
lst=list()
for i in range(0,n):
    temp=int(input())
    lst.append(temp)
print("Before Swap")
print(lst)
lst[0],lst[n-1]=lst[n-1],lst[0]
print("After Swap")
print(lst)