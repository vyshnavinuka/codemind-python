def fact(a):
    s=1
    for i in range(1,a+1):
        s=s*i
    return s
n=int(input())
k=m=0
e=n
while e:
    k=e%10
    m=m+fact(k)
    e=e//10
if m==n:
    print("The number %d is a strong number"%n)
else:
    print("The number %d is not a strong number"%n)