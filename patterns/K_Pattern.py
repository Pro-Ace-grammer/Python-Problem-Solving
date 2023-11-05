
'''
to print K
'''

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==1) or (j==(n-i)) or (i>=(n+1)//2 and j==(i-1)):
             print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
