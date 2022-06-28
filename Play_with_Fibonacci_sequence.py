x=int(input())
i=0
a=0
b=1
d=2
print(a,end=" ")
print(b,end=" ")
while x>0:
    c=a+b
    d+=1
    a=b
    b=c
    print(c,end=" ")
    if d==x:
        break