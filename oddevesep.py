n=int(input())
lste=list()
lsto=list()
boxe=0
boxo=0
for i in range(0,n):
    temp=int(input())
    if temp%2==0:
        lste.append(temp)
        boxe=boxe+1
    else:
        lsto.append(temp)
        boxo = boxo + 1

print("Even List")
print(lste,"Count=",boxe)
print("Odd List")
print(lsto,"Count=",boxo)
