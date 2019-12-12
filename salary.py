salary=int(input())
if (salary<15000):
    hra=0.15*salary
    da=0.90*salary
else:
    hra=5000
    da=0.98*salary

print("GrossSalary:",salary+hra+da)