'''
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
'''
n = int(input())
for i in range(0,n):
    if i%2 == 0:
        print('0 '*n)
    else:
        print('1 '*n)
