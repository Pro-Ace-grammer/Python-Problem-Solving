'''
this program is so check whether the given number is an armstrong number or not
the logic is..... if we take each digit of a number and cube it and we add all the cubed numbers and if it comes or it is equal to the original number then it is an armstrong number
'''
n = int(input())
temp = n
rem = 0
sum = 0
l = len(str(n))
while temp>0:
    rem = temp%10
    sum+= rem**l
    temp//=10
if sum == n:
    print(n,'is an Armstrong number')
else:
    print(n,'is not an Armstrong number')


# The same program can be also written in using for loop as bewlow
# n = int(input())
# temp = n
# sum1 = 0
# for i in range(0,len(str(n))): # i will go from 0 - len-1 ex: n=153 then len = 3 so i will go 0 - 2
#     sum1+= (temp%10)**len(str(n))  # we take each number and power it to no. of digits
#     temp//=10
# if sum1 == n:
#     print('It is an Armstrong number')
# else:
#     print('It is not a Armstrong number')