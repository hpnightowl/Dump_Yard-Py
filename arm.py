import math as m
x=int(input())
y=x;
sum=0
while(x!=0):
    rem =int(x%10)
    sum=sum+m.pow(rem,3)
    x=x/10

if(y==sum):
    print("💪💪Armstrong")
else:
    print("LOL")