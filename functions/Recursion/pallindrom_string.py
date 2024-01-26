'''
program to check if the giver string is pallindrome or not
'''

def palin(st):
    if len(st) <= 1:
        print('Palindrome')
    else:
        if st[0]==st[-1]:
            palin(st[1:-1])
        else:
            print('Not Palindrome')

palin(input("Enter a string: "))