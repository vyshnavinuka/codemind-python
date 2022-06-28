n=int(input())
a=list(map(int,input().split()))
z=[]
for i in range(n-1):
    a.pop(0)
    m=max(a)
    z.append(m)
z.append("-1")
print(*z)