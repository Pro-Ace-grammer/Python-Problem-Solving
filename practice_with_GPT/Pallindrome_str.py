'''
Write a Python function that checks if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequences of characters that reads the same forwards and backward (ignoring spaces and capitalization).
For example, "A man a plan a canal Panama" is a palindrome because it reads the same when spaces and capitalization are ignored.
'''

# def palli(st):
#     temp=''
#     for i in st:
#         if i == ' ':
#             continue
#         else:
#             temp+= i.lower()
#     return temp == temp[::-1]

# print(palli(input('str: ')))


# ORRR


def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()

    # Check if the modified string is equal to its reverse
    return s == s[::-1]

# Test the function
input_str = input('Enter a string: ')
result = is_palindrome(input_str)

if result:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
