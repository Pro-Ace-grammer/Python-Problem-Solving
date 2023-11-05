'''
To print J
'''
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==1 and j not in (1,n)) or (j==(n+1)//2) or (i==n and j<=(n+1)//2) or (j==1 and i>(n+1)//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


'''
or (j==(n+1)//2) or (i==n or j<=(n+1)//2) or (j==1 and i>(n+1)//2)
'''
