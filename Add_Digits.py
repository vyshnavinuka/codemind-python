x=int(input())
k=0
while x!=0:
    d=x%10
    x=x//10
    k=k+d
    if k>9 and x==0:
        x=k
        k=0
print(k)