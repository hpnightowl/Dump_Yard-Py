n=int(input())
box = 0
for i in range(1, n):
    if n % i == 0: box = box + 1

if box < 2:
        print("Prime")
else:
        print("Not Prime")
