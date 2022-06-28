x=int(input())
l=list(map(int,input().split()))
z=0
h=0
for i in l:
    k=l.count(i)
    if(k==1):
        h+=1
        if i>z:
            z=i
if(h==0):
    print("-1")
else:
    print(z)