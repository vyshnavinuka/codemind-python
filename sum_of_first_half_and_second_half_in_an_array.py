n=int(input())
arr=list(map(int,input().strip().split()))
k=n//2
s1=0
s2=0
for i in range(0,k):
    s1=s1+arr[i]
for i in range(k,n):
    s2=s2+arr[i]
print(s1)
print(s2)