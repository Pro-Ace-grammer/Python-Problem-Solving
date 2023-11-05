'''
Programs to Implement LIST COMPREHENSION ONLY
'''

#Comprehension in python is a short and concise way to construct new sequences such as list, set, dictionary


#---------------------SIMPLE LIST COMPREHENSION------------------------#
#SYNTAX:  [outer/expression for var in iterable]

#Program to construct list of squares of 10 numbers
# sqr = [i**2 for i in range(1,11)]
# print(sqr)


# Program to C.L. of sum of square and cube of all the numbers
# sqr_cube_sum = [(i**2)+(i**3) for i in range(1,20)]
# print(sqr_cube_sum)

#C.L of even numbers without condition
# even_li = [i for i in range(0,21,2)]
# print(even_li)

# c.l of negative odd numbers
# odd_neg = [i for i in range(-19,0,2)]
# print(odd_neg)



#----------------- SIMPLE 'IF' LIST COMPREHENSION---------------------#
#SYNTAX:    [TSB for var in iterable if<condition>]

# to find out even nos using if statement
# even_if = [i for i in range(0,20) if i%2==0]
# print(even_if)

# To convert vowels into Uppercase char
# st = 'i love you babiee'
# out = [chr(ord(i)-32) for i in st if i in 'aeiou']
# print(out)

# To convert Consonants into Uppercase char
# st = 'i love you babiee'
# out = [chr(ord(i)-32) for i in st if i not in ' aeiou']
# print(out)




#----------------- SIMPLE 'IF - ELSE' LIST COMPREHENSION---------------------#
# SYNTAX:   [TSB if<condition>  else (ESB) for var in iterable]

#input = [10,20,30,40,50]
#output = [333, 8001, 9000, 64001, 41666]
# input = [10,20,30,40,50]
# out = [(input[i]**3)//3 if i%2==0 else (input[i]**3+1) for i in range(len(input))]
# print(out)


#[1000, 1, 1002, 3, 1004, 5, 1006, 7, 1008, 9]
# out = [(i+1000) if i%2==0 else i for i in range(10)]
# print(out)


#Print the previous character if it is a consonant or next otherwise
# st = 'ISLoveSyous'
# out = [chr(ord(i)+1) if i in 'aeiouAEIOU' else chr(ord(i)-1) for i in st]
# print(out)


#to check if the given number is even or odd without using modulous

 
