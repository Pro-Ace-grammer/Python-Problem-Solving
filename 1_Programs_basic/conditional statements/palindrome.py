'''
To check if the number is palindrom or not 
the logic is ... if we reverse a given number and it is equal to the original number then it is a palindrome number
'''

# n = int(input())
# rev = 0
# temp = n
# while temp>0:
#     rev = rev*10 +(temp%n)
#     temp = temp // 10
# if rev == n:
#     print(n,'is a palindrome number')
# else:
#     print(n,'is not a palindrome number')


# Same program using for loop
n = int(input())
rev = 0
temp = n
for i in range(len(str(n))):
    rev=(rev*10)+(temp%10)
    # print(rev,temp%10,temp,sep=' - ')
    temp//=10
# print(rev==n)
if rev==n:
    print('It is Palindrome')
else:
    print('It is not Palindrome')