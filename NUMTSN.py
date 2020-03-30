# cook your dish here
# your code goes here
t = int(input())
while t!=0:
    counter=0
    x, y = [int(x) for x in input().split()]
    for i in range(x,y+1):
        thcount=0
        secount=0
        nicount =0
        while i!=0:
            rem = i%10
            if rem == 3:
                thcount = thcount + 1
            if rem == 6:
                secount = secount + 1
            if rem == 9:
                nicount = nicount + 1
            i=i//10
        if(thcount==secount and thcount==nicount and secount==nicount and secount!=0 and nicount!=0 and thcount!=0):
            counter=counter+1
    print(counter)
    t=t-1
