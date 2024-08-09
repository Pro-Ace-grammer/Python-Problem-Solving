n = 5
for i in range(0,n+1):
    print('  '*(n-i),end='')
    print('* '*i)

for i in range(1,n):
    print('  '*i,end='')
    print('* '*(n-i))
'''
*
* *
* * *
* * * *
* * * * *
'''
