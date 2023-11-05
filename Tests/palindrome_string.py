'''
This program takes a string and checks whether it is palindrome or not ignoring the case
'''

def pallin(st):
    temp = ''
    for i in st:
        if 'A'<=i<='Z' or 'a'<=i<='z':
            temp+= i.lower()
    if temp == temp[::-1]:
        return True
    else:
        return False

a = pallin(input('Enter a string: '))
print(a)
