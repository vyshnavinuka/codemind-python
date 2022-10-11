n,m=map(int,input().split())
s=0
for i in range(n):
    a=list(map(int,input().split()))
    s+=sum(a)
print(s)