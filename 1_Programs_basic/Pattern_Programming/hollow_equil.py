'''
'''
n = int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(end = ' ')
    for k in range(0, i):
        if (k == 0) or (k ==i-1) or (i==n):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()