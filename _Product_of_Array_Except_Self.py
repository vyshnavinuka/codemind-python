x=int(input())
l=list(map(int,input().split()))
k=1
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]==l[j]:
            continue
        else:
            k=k*l[j]
    print(k,end=" ")
    k=1