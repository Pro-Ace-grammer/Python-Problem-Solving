'''
to print the pattern M
'''

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or (i ==j and j<=(n+1)//2) or (j== (n+1)-i and i<=(n+1)//2) or (j==n):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
 
