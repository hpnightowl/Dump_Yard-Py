#comparefunction
def cmp(a, b):
    return (a > b) - (a < b)

#1
n=int(input())
for i in range(1,6):
    print(n,"*",i,"=",n*i)
    
#2
n=int(input())
for i in range(1,n+1):
    print(i,end=",")

#3
n=int(input())
for i in range(1,n+1):
    print(i,end=' ')

#4
for i in range(0,11):
    print(i*i,end=' ')

#5
sum=0
for i in range(0,11):
    if i%2==0:
        sum+=i
print("Sum of Even Numbers From 0 to 10: ",sum)

#6
sum=0
lst=list(input("Enter Numbers to add in list"))
for i in lst:
    sum+=int(i)
print("Sum Of Number in List: ",sum)

#7
lst=list(input("Enter Elements in List To Find Maximum: "))
print("The Largest Element in this list is: ",max(lst))

#8
str1="this is a sample DaTaa"
if 'is' in str1:
    print("Found")
else:
    print("Nope")

#9
n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("Enter Your Choice:")
ch=int(input())
if ch ==1 :
    print("Addition of two numbers = ",n1+n2)
if ch ==2 :
    print("Subtraction of two numbers = ",abs(n1-n2))
if ch ==3 :
    print("Multiplication of two numbers = ",n1*n2)
if ch ==4 :
    print("Division of two numbers =",n1/n2)

#10
n=int(input("Till What Number You Want Sum of Natural Numbers: "))
print("Sum of Natural Numbers till",n,"=",int(n*(n+1)/2))

#11
tup=tuple(input("Enter Tuple 1 Elements: "))
tup1=tuple(input("Enter Tuple 2 Elements: "))
#i
print("Maximum element in tuple: ",max(list(tup)))
#ii
print("Minimum element in tuple: ",min(list(tup)))
#iii
print("Sum of two tuples: ",tup+tup1)
#iv
tup4=tup
print("Copied Tuple: ",tup4)
#v
print("Slice Part Of Tuple: ",tup[0:2])
#vi
print("Converted To List: ",list(tup))
#vii
print("Comparision of tuples: ",cmp(tup,tup1))
#viii
tup2={1,4,'a',2}
tup3={'a',4,'abc',2.0}
print("Different Data Type Tuples")
print(tup2)
print(tup3)


#12

n=[1,2,3,4,5,6,7,8,9,10]
even=0
odd=0
for i in n:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Odd:",odd)
print("Even:",even)





