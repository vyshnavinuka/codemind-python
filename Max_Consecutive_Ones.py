n=int(input())
a=list(map(int,input().split()))
z=[]
c=0
k=0
for i in a:
    if i==1:
        k=1
        c+=1
    else:
        z.append(c)
        c=0
z.append(c)
m=max(z)
print(m)