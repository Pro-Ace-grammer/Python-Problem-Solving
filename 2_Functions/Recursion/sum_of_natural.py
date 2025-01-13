'''
write a recursive function to find the sum of n natural numbers
'''

def sum_natural(n):
    if n<=1:
        return n
    else:
        return n + sum_natural(n-1)
    
print(sum_natural(int(input('Enter the number'))))