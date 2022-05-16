num,mum=map(int,input().split())
for i in range(1,mum+1):
    if i%2!=0:
        print(num, 'x', i, '=', num*i)