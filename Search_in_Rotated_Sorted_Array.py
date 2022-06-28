x=int(input())
l=list(map(int,input().split()))
z=int(input())
c=0
for i in range(len(l)):
    if l[i]==z:
        c+=1
        print(i)
if(c==0):
    print("-1")