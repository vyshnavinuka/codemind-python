x=int(input())
l=list(map(int,input().split()))
z=int(input())
k=max(l)
for i in l:
    n=i+z
    if(n>=k):
        print("True",end=" ")
    else:
        print("False",end=" ")