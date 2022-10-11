a,b=map(int,input().split())
n=[]
for i in range(a):
    z=list(map(int,input().split()))
    n.append(sum(z))
print(*n)