def pal(a):
    n=a
    t=s=0
    while a:
        t=a%10
        s=(s*10)+t
        a=a//10
    if s==n:
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
c=s=zap=0
for i in range(0,n):
    if pal(a[i])==1:
        c+=1
print(c)