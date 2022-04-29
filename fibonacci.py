n=int(input())
n1=0
n2=1
print(n1,n2,end=' ')
for i in range(n-2):
    m=n1+n2
    n1=n2
    n2=m
    print(m,end=' ')