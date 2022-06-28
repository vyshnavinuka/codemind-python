x=int(input())
l=list(map(int,input().split()))
z=int(input())
c=0
k=0
for i in range(len(l)):
    if l[i]==z:
        c+=1
        print(i,end=" ")
        break
for i in range(len(l)-1,-1,-1):
    if l[i]==z:
        k+=1
        print(i,end=" ")
        break
if(c==0):
    print("-1",end=" ")
if(k==0):
    print("-1",end=" ")
