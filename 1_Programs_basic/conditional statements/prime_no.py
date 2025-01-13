'''
to check if the given number is prime or not
'''
# n = int(input())
# c = False
# if n>1:
#     for i in range(2,n//2+1):# for time complexity remember this that only uptill n/2 numbers can divide n
#         if n%i==0:
#             c = True
#             break
# if c:
#     print(n,'is not a prime number')
# else:
#     print(n,'is a prime number')


# same progrm using while loop
n = int(input('n: '))
flag = True
if n>1:
    i = 2
    while i < n//2+1:   # for time complexity remember this that only uptill n/2 numbers can divide n
        if n%i == 0:
            flag = False
            break
        i+=1
elif n == 1:
    flag = False
if flag:
    print('It is a Prime number')
else:
    print('It is not a prime number')