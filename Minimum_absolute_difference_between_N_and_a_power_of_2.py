def test(a):
    for i in range(int(a**0.5)+1):
        if(2**i)==a:
            return 1
    return 0
    
n=int(input())
k=0
if test(n)==1:
    print("0")
else:
    for i in range(n):
        if(2**i)>n:
            k=2**i
            break
    z=k//2
    if k-n>=n-z:
        print(n-z)
    elif k-n<n-z:
        print(k-n)