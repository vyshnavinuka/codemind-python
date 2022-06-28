x=int(input())
for i in range(x):
    y=int(input())
    s=0
    t=(y*(y+1))//2
    z=list(map(int,input().split()))
    for i  in z:
        s=s+i;
    k=t-s
    print(k)