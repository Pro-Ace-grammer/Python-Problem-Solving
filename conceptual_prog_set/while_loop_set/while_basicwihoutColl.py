'''
1. Write a program to print numbers from 1 to 10.
'''
# i = 1
# while i <=10:
#     print(i)
#     i+=1

'''
2. Write a program to calculate the sum of first 10 natural number.
'''
# s1 = 0
# i = 1
# while i <=10:
#     s1+=i
#     i+=1
# print(s1)


'''
Question 3
Write a program that prompts the user to input a positive integer. It should then print the multiplication table of that number. 
'''
# n = int(input('n: '))
# i = 0
# while i <=10:
#     print(f'{n} x {i} = ',n*i)
#     i+=1

'''
Question 4
Write a program to find the factorial value of any number entered through the keyboard. 
'''
# n = int(input('n: '))
# i = 1
# facto = 1
# while i <= n:
#     facto *= i
#     i+=1
# print(facto)


'''
Question 5
Two numbers are entered through the keyboard. Write a program to find the value of one number raised to the power of another. 
'''
#the task here is to we have to find the number raised to power without using the exponent operator
# a = int(input('n: '))
# b = int(input('power: '))
# i = 1
# vpow = 1
# while i <= b:
#     vpow *= a
#     i += 1
# print(vpow)


'''
Question 6
Write a program that prompts the user to input an integer and then outputs the number with the digits reversed. For example, if the input is 12345, the output should be 54321.
'''
# n = int(input('n: '))
# temp = n
# rev = 0
# while temp != 0:
#     rev = rev*10 + (temp%10)
#     temp//=10
# print(rev)


'''
Question 7
Write a program that reads a set of integers, and then prints the sum of the even and odd integers.
'''
# This program can be solved using for 
# l1 = {1,235,4,3,41,54,7,67,2,546,8767,76,14,739}
# print(l1)

'''
Question 8
Write a program that prompts the user to input a positive integer. It should then output a message indicating whether the number is a prime number.
'''
# n = int(input('n: '))
# i = 2
# flag = True
# while i<n:
#     if n%i ==0:
#         flag = False
#         break
#     i+=1
# if flag:
#     print('It is a prime  number')
# else:
#     print('It is not a prime number')


'''
Question 9
Write a program to calculate HCF of Two given number.
'''
#using while approach
# a = int(input('a: '))
# b = int(input('b: '))
# if a<b:
#     n = a
# else:
#     n = b
# while n>0:
#     if a%n==0 and b%n==0:
#         break
#     n-=1
# print(n)


'''
Question 10
Write a do-while loop that asks the user to enter two numbers. The numbers should be added and the sum displayed. The loop should ask the user whether he or she wishes to perform the operation again. If so, the loop should repeat; otherwise it should terminate. 
'''
#pending ...........


'''
Question 11
Write a program to enter the numbers till the user wants and at the end it should display the count of positive, negative and zeros entered. 
'''
# cp = 0
# cn = 0
# cz = 0
# flag = True
# while flag:
#     n = int(input('Enter a number: '))
#     if n > 0:
#         cp += 1
#     elif n==0:
#         cz += 1
#     else:
#         cn += 1 
#     i = input('do you want to conitue? y/n: ')
#     if i in 'yY':
#         flag = True
#     else:
#         flag = False
# print('No of zero: ',cz)
# print('No of positive: ',cp)
# print('No of negative: ',cn)


'''
Question 12
Write a program to enter the numbers till the user wants and at the end the program should display the largest and smallest numbers entered.
'''
# lar = 0
# small = 1000
# flag = True
# while flag:
#     n = int(input('n: '))
#     if lar < n:
#         lar = n
#     if small > n:
#         small = n
#     i = input('Do you want to continue? y/n: ')
#     if i not in 'yY':
#         flag = False
# print('Larger number: ',lar)
# print('Smaller number: ', small)


'''
Question 13
Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number.
For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )
'''
#This code may take a some time to execute depending upon the range specified
# 153
# temp = 1 s1 = 27+ 125 + 1** 
# i = 1
# while i < 500:
#     l = len(str(i))
#     s1 = 0
#     temp = i
#     while temp >0:
#         s1 += (temp%10)**l
#         temp //=10
#     if i == s1:
#         print(i)
#     i+=1


'''
Question 14
Write a program to print Fibonacci series of n terms where n is input by user :
0 1 1 2 3 5 8 13 24 ..... 
'''
# a = 0
# b = 1
# c = 0
# n = int(input('n: '))
# i=0
# while i < n:
#     c = a+b
#     print(a,end=' ')
#     a = b
#     b = c
#     i+=1


'''
Question 15
Write a program to calculate the sum of following series where n is input by user. 
1 + 1/2 + 1/3 + 1/4 + 1/5 +…………1/n 
'''
# n = int(input('n: '))
# i = 1
# s1 = 0
# while i <= n:
#     s1+= round(1/i,5)
#     i+=1
# print(s1)


'''
Question 16
Compute the natural logarithm of 2, by adding up to n terms in the series
1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n
where n is a positive integer and input by user.
example:
n: 5
0.7833333333333332
'''
# n = int(input('n: '))
# sign = 1    # this will basically store the sign either - or +
# log = 0
# i = 1
# while i <= n:
#     log = log + (sign*(1/i))
#     sign = -1*sign  # the series is alternate on - and + so we multiply it with -1 to get alternate signs
#     i+=1
# print(log)


'''
Question 17
Write a program that generates a random number and asks the user to guess what the number is. If the user's guess is higher than the random number, the program should display "Too high, try again." If the user's guess is lower than the random number, the program should display "Too low, try again." The program should use a loop that repeats until the user correctly guesses the random number.
'''
# import random as r
# a = r.randint(0,11)
# while True:
#     n = int(input('Guess the number: '))
#     if n == a:
#         print('well guessed')
#         break
#     else:
#         print('Try again!!')



