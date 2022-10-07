l=list(map(str,input().split()))
for i in l:
    m=ord(min(i))
    n=ord(max(i))
    print(n-m,end=" ")