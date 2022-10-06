n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in range(n):
    if l[i]>=a and l[i]<=b:
        k.append(l[i])
if len(k)>0:
    print(max(k))
else:
    print(-1)