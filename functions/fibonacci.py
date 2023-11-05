'''
Python function to print the N fibonacci series
example:
n = 10
0 1 1 2 3 5 8 13 21 34
'''

def fibo(n):
    a = 0
    b = 1
    sum = 0
    print(a,b,end=' ')
    for i in range(3,n+1):
        sum = a+b
        print(sum,end=' ')
        a = b
        b = sum
        

fibo(int(input('n :')))