'''
Python Program to find whether the given two string are anagram or not
example:
st1 = silent
st2 = listen
True 
'''

#So basically two strings are anagram if the len of strings are same and it has the same characters present in another string
st1 = input('st1: ')
st2 = input('st2: ')
if sorted(st1) == sorted(st2): #sorting elements in a
    print(True)
else:
    print(False)