'''
python function to find the factorial of a given number
example:
a = 4
factorial = 24
'''

def facto(n):
    i,fact = 1,1
    while i<=n:
        fact*=i
        i+=1
    return fact

fact = facto(int(input('n: ')))
print(fact)