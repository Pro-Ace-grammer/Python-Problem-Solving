'''
Alphabet F
'''

n = int( input ())
for i in range(1, n+1):
    for j in range(1,n+1):
        if (i==1)or (i==(n+1)//2 and j!=n) or (j==1):
            print('*',end=' ')
        else:
            print(' ', end = ' ')
    print()

