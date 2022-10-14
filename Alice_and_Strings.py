n=int(input())
for k in range(n):
    s1,s2=input(),input()
    if(len(s1)==len(s2)):
        for i in range(len(s1)):
            if(s1[i]>s2[i]):
                print('NO')
                break
        else:
            print('YES')
    else:
        print('NO')