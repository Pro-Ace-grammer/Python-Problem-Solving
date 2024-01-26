# To check if input is Prime Number
'''
n = int(input('Enter a number'))
if n > 1:
    for i in range(2,n//2):
        if n%i == 0:
            print(n,'is not a Pime number')
            break
    else:
        print(n,'is prime number')
else:
    print('Invalid Input')
'''



# To Find Factorial of a number
'''
n = int(input('Enter the number'))
facto = 1
if n == 1:
    print('Factorial: 1')
elif n==0 or n < 0 :
    print('Factorial: 0')
else:
    for i in range(2,n+1):
        facto*=i
    print(facto)
'''



# To print the Fibonacci Series
'''
a = 0
b = 1
n =  int(input('Enter the no of series: '))

i = 1
while i <= n:

    print(a, end='  ')
    a,b = b, a+b
    i+=1
'''