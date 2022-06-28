n=int(input())
a=list(map(int,input().split()))
mx=-1000
for z in range(n-1):
    for i in range(n):
        for j in range(i,n):
            s=sum(a[i:j+1])
            if s>mx:
                mx=s
    tm=a[0]
    a[0]=a[-1]
    for i in range(1,n):
        f=a[i]
        a[i]=tm
        tm=f
print(mx)
    