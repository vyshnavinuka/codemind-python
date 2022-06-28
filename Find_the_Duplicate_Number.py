x=int(input())
l=list(map(int,input().split()))
for i in l:
    k=l.count(i)
    if k>1:
        print(i)
        break