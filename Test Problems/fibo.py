
def fibo(n):
    a = 0
    b = 1
    print(a,b,end=' ')
    sum = a+b
    while sum<=n:
        print(sum,end=' ')
        sum = a+b
        a = b
        b = sum
fibo(int(input('Enter a number: ')))

