x=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    for j in l:
        if i>j:
            c+=1
    print(c,end=" ")
    c=0