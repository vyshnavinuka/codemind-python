x=int(input())
l=list(map(int,input().split()))
t=[]
for i in l:
    k=i*i
    t.append(k)
print(*sorted(t))