n = int(input())
for i in range(0,n):
    for j in range(1,n+1):
        if(j== (n-i)) or (j==n) or (i==n-1):
             print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
