n=int(input())
w=list()
for i in range(0,n):
    x=int(input())
    w.append(x)

for i in range(0,n):
     x=bool(all(w[i] > w[i+1]) or all(w[i] > w[i+1]))

print(x)

