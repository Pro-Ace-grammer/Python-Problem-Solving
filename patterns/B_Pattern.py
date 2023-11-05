''' To print the pattern of alphabet B'''
n = int( input ())
for i in range(1, n+1):
    for j in range(1,n+1):
        if (i==1 and j!=n) or (j == 1) or (i == (n+1)//2 and j != n) or (i == n and j != n) or (j==n and i not in (1,(n+1)//2,n)):
           print('*',end=' ')
        else:
            print(' ', end = ' ')
    print()


*
* *
* * *
* * * *
* * * * *
