'''
python function to find the GCD of 2 numbers or HCF of two numbers

example:
a = 4
b = 10
output = 2

So basically HCF or GCD is the highest common divisor of the numbers in this case it is 2 
i.e. 4/2 and 10/2
'''

def gcd(a,b):
    if a<b:
        n = (a+1)//2
    else:
        n = (b+1)//2

    for i in range(1,n+1):
        if a%i==0 and b%i==0:
            g = i
    return g

n = gcd(int(input('a: ')),int(input('b: ')))
print('gcd =',n)