'''
Recursive function to check if the number is pallindrome or not
'''

# def rev(n,temp=0):
#     if n==0:
#         return temp
    
#     temp = (temp * 10) + (n%10)
#     return rev(n//10,temp)

# n = int(input('Enter a number: '))

# if n == rev(n):
#     print('Palliiii')
# else:
#     print('Not Palliiiii')



# Example 7: Pallindrom string
def isPallin(st):
    if len(st)<=1:
        return True
    elif st[0] != st[1]:
        return False    
    else:
        return isPallin(st[1:-1]) # Shortening the string by removing first and last char
    
print(isPallin('Hello'))
