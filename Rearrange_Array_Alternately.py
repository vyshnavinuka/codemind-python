def rearrange(arr,n):
    temp=n*[None]
    small,large=0,n-1
    flag=True
    for i in range(n):
        if flag is True:
            temp[i]=arr[large]
            large-=1
        else:
            temp[i]=arr[small]
            small+=1
        flag=bool(1-flag)
    for i in range(n):
        arr[i]=temp[i]
    print(*arr)
x=int(input())
for i in range(x):
    n=int(input())
    a=list(map(int,input().split()))
    rearrange(a,n)