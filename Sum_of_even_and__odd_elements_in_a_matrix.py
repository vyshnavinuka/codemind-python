n,m=map(int,input().split())
c=0
s=0
for i in range(n):
    a=list(map(int,input().split()))
    for i in a:
        if i%2==0:
            c+=i
        else:
            s+=i
print(c,s)