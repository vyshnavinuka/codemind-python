x=int(input())
temp=x
c=0
k=0
s=0
for i in range(1,x+1):
    if x%i==0:
        c+=1
    if c==2:
        while temp>0:
            d=temp%10
            temp=temp//10
            k=k*10+d
        for j in range(1,k+1):
            if k%j==0:
                s+=1
if s==2 and c==2:
    print("circular prime")
elif s==2 or c==2:
    print("prime but not a circular prime")
else:
    print("not prime")