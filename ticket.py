tcost=int(input())
no_t=int(input())
totalcost=int()
if(no_t < 50):
    totalcost=tcost
elif(no_t >= 50 and no_t <=100):
    totalcost=tcost-tcost*0.1
elif(no_t >=101 and no_t <=200):
    totalcost=tcost-tcost*0.2
elif(no_t >=201 and no_t <=400):
    totalcost=tcost-tcost*0.3
elif(no_t >=401 and no_t <=500):
    totalcost=tcost-tcost*0.4
elif(no_t >=501 ):
    totalcost=tcost-tcost*0.5

print("Cost Of Tickets After Discount and GST :",totalcost)