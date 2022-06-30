n=int(input())
arr=list(map(int,input().strip().split()))
k=[]
for i in range(n):
    if arr[i]%2==0:
        if arr[i] not in k:
            k.append(arr[i])
print(len(k))