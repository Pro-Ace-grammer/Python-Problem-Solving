'''
to find the lcm of two given numbers
example
a = 2
b = 8
output = 16
'''

def lcm(a,b):
    if a>b:
        n = a*2
    else:
        n = b*2
    for i in range(n,(a*b)+1):
        if i%a==0 and i%b==0:
            return i

n = lcm(int(input('a: ')),int(input('b: ')))
print('lcm =',n)