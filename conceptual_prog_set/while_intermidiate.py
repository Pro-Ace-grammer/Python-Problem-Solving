def tolist(st):    #function to be used to convert comma saperated string to list
    l1 = st.split(',')
    l2 = []
    for i in l1:
        l2+=[int(i)]
    return l2



'''
python program to find the sum of integers in an array or a list
Algo:
1- we first take an input of comma saperated string and convert it into a list
2- initialize i=0 and sum variable s1=0
3- iterate the list and find the sum of each element and update the looping variable
4- print the sum

time complexity: O(n)
'''
# l1 = tolist(input('Enter comma saperated: '))
# i = 0
# s1 = 0
# while i < len(l1):
#     s1+=l1[i]
#     i+=1
# print(s1)



'''
Python program to find the sum digits of integers in a given array or list
example:
in = [12,32,543,23,563,768]
out = [3, 5, 12, 5, 14, 21]
1- we first take an input of comma saperated string and convert it into a list
2- initialize i=0 and a res variable to store the list of numbers 
3- iterate the list and store the current element(integer) in a temp variable and take s1 to store the sum of digit 
4- Iterate into another loop until the temp=0 
5- find the sum of digit of the current element
6 - append the sum into 'res' list
6- print the result (res)
'''
# l1 = tolist(input('enter comma saperated integers: '))
# i = 0
# res = []
# while i < len(l1):
#     temp = l1[i]
#     s1 = 0
#     while temp > 0:
#         s1 +=(temp%10)
#         temp //= 10
#     res.append(s1)
#     i+=1
# print(res)


'''
python function to find the GCD of 2 numbers or HCF of two numbers
example:
a = 4
b = 10
output = 2
So basically HCF or GCD is the highest common divisor of the numbers in this case it is 2 
i.e. 4/2 and 10/2
'''
# a = int(input('a: '))
# b = int(input('b: '))
# if a<b:
#     n = a
# else:
#     n = b
# i = n
# while i <= n:
#     if a%i==0 and b%i==0:
#         print('HCF:',i)
#         break
#     i-=1


'''
To find the lcm of three numbers
'''
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# if a>b and a>c:
#     i = a
# elif b>c:
#     i = b
# else:
#     i = c
# while i <= a*b*c:
#     if i%a==0 and i%b==0 and i%c==0:
#         print(i)
#         break
#     i+=1



'''
To find the perfect numbers between the range 1-500
 - Perfect number is a number whose sum of all the factors of number is equal to the number.
1 - initialize i=1 range in while condition as i < 500
2 - find each numbers factors and sum them up excluding the number
3 = check if the sum is equal to the original number the either store or print the number
'''
# i = 1
# perfect = []
# while i < 500:
#     s1 = 0
#     j = 1
#     while j <= (i//2 + 1):
#         if i%j==0:
#             s1 += j
#         j+=1
#     if s1 == i:
#         perfect.append(i)
#     i+=1
# print(perfect)  #output = [1, 6, 28, 496]


'''
Write a program to print following :

i)
**********
**********
**********
**********

ii)
*
**
***
****
*****

iii)
        *
      **
    ***
  ****
*****

iv)
        *
      ***
    *****
  *******
*********

v)
     *
    * *
   * * *
  * * * *
 * * * * *

vi)
        1
      222
    33333
  4444444
555555555

vii)
        1
      212
    32123
  4321234
543212345
'''

# 1st Pattern from above
# n = int(input('n: '))
# i = 0
# while i < n:
#     print("* "*n)
#     i+=1


# 2nd Pattern from above
# n = int(input('n: '))
# i = 1
# while i <= n:
#     print('* '*i)
#     i+=1


# 3rd Patter from above
# n = int(input('n: '))
# t = n*2-1     #since we need a cross pattern and the no of spaces is doubled
# i = 1
# while i <=n:
#     print(' '*t,end = '')
#     print('*'*i) #no space between the stars
#     t-=2
#     i+=1
    

# 4th Patter from above
# n = int(input('n: '))
# t = n
# i = 1
# while i <=n:
#     print(' '*t,end = '')
#     print('*'*i)
#     t-=1
#     i+=1
    

# 5th Pattern from above
# n = int(input('n: '))
# t = n
# i = 1
# while i <=n:
#     print(' '*t,end = '')
#     print('* '*i)
#     t-=1
#     i+=1



'''
Question 19
Write a program to compute sinx for given x. The user should supply x and a positive integer n. We compute the sine of x using the series and the computation should use all terms in the series up through the term involving 
sin x = x - x3/3! + x5/5! - x7/7! + x9/9! .......
'''

# below is a recursive function to find the factorial of a number this is something extra which I have done
#we may choose to directly run a while loop inside our main while loop of this program to find the denominator factorial
# def fact(i):
#     if i == 1:
#         return 1
#     else:
#         return i*fact(i-1)
    
# x = int(input('x: '))
# n = int(input('n: '))
# i = 1
# sign = 1
# sin = 0    #this will store the alternate signs either - or +
# while i <=n:
#     sin = sin +(sign * (x*i/fact(i)))
#     sign *= -1
#     i+=1
# print(sin)


'''
Write a program that makes the user guess a particular number between 1 and 100. Save the number to be guessed in a variable called magic_number.
If the user guesses a number higher than the secret number, you should say Too high!. Similarly, you should say Too low! if they guess a number lower than the secret number. Once they guess the number, say Correct!
'''
