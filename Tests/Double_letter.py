'''
Write a Python function that takes a sentence as input and determinewhether any words in the sentences contain duplicatee letters. If the sentence contains any such word, the funstion should return True; Otherwise , it should return False.
    input: "Python Programming is a funny language"
    output: True
    input: " I am very lucky to have you"
    output: Flase
This program returns True if any word in the string contains Duplicate consecutive letters
'''

def double(str1):
    temp = ''
    l1 = str1.split(' ')
    for i in l1:
        for k in i:
            if k in temp:
                return True
            else:
                temp+=k
        temp=''
    return False

a = double(input('Input a string: '))
print(a)