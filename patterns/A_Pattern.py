n = int( input ())
for i in range(1, n+1):
    for j in range(1,n+1):
        if (i==1 and j not in (1,n)) or (j == 1 and i!=1) or (i == (n+1)//2) or (j==n and i != 1):
            print('*',end=' ')
        else:
            print(' ', end = ' ')
    print()
