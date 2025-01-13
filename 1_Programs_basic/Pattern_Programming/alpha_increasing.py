'''
A
B B
C C C
D D D D
E E E E E
'''

'''
n = int(input())
for i in range(1,n):
    cr = chr(64+i)
    print(cr*i)
'''

n = int(input())
a = ord('A')
for i in range(1,n+1):
    print(f'{chr(a)} '*i)
    a+=1
