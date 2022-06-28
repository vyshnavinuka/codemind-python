x=int(input())
l=list(map(int,input().split()))
k=0
for i in l:
    c=0
    while i:
        d=i%10
        i=i//10
        c+=1
    if(c%2==0):
        k+=1
print(k)