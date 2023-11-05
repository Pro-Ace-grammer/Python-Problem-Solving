'''
1 0 1 0 1 0
0 1 0 1 0 1
1 0 1 0 1 0
0 1 0 1 0 1
1 0 1 0 1 0
0 1 0 1 0 1
'''
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i%2 == 1 and j%2 == 1) or (i%2 == 0 and j%2 == 0):
            print('1 ', end=' ')
        else:
            print('0 ', end= ' ')
    print()
    
