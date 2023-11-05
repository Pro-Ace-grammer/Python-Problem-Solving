'''
Python Recursive function to find the factorial of a number
'''

def facto(n):
    if n ==1 :
        return 1
    elif n == 0:
        return 0
    else:
        return n*facto(n-1)
    return n

print(facto(int(input('Enter a number: '))))