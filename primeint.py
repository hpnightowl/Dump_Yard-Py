print("Enter The Range (Upper)")
x=int(input())
print("Enter The Range (Lower)")
y=int(input())

def prime(i):
    box = 0
    for x in range(1, i):
        if i % x == 0: box = box + 1
    if box < 2:
        return i

for i in range(2,y):
    hp=prime(i)
    print(hp,)
#returning none


