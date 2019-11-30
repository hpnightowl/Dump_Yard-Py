import math as m
print("Enter Principle Value ",end="")
p=int(input())
print("Enter Rate Value ",end="")
r=int(input())
print("Enter Time Value ",end="")
t=int(input())
ci=m.pow(p*(1+r/100),t)
print("Compund Interest =",ci)
