n=int(input())
arr=list(map(int,input().strip().split()))
if n%2!=0:
    arr.append(0)
print(*arr)