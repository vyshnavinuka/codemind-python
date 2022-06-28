x=int(input())
k=int(input())
for i in range(0,k+1):
    a,b=map(int,input().split())
    if a>=x and b>=x:
        if a==b:
            print("ACCEPTED")
        else:
            print("CROP IT")
    else:
        print("UPLOAD ANOTHER")