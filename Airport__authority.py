x=int(input())
c=0
k=[]
for i in range(x):
    z=int(input())
    k.append(z)
y=int(input())
for j in k:
    if j<=y:
        c=c+1
    else:
        c=c+2
print(c)