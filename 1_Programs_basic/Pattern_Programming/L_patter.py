'''
to print the letter L
'''

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or (i ==n and j<=(n+1)//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
