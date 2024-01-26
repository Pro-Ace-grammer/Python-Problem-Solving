def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))

n = int(input('Enter how many terms: '))
if n<=0:
    print('Please enter a positive number')
else:
    print('Fibonacci Sequence')
    for i in range(n):
        print(fibo(i))