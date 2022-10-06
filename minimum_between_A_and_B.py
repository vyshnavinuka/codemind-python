n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in range(n):
    if arr[i]>=a and arr[i]<=b:
        k.append(arr[i])
if len(k)>0:
    print(min(k))
else:
    print(-1)