'''
to find the nth fibo

F(0) = 0 (1st number)
F(1) = 1 (2nd number)
F(2) = 1 (3rd number)
F(3) = 2 (4th number)
F(4) = 3 (5th number)
F(5) = 5 (6th number)
F(6) = 8 (7th number)
F(7) = 13 (8th number)
F(8) = 21 (9th number)
F(9) = 34 (10th number)
F(10) = 55 (11th number)
'''

def fibo(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
print(fibo(int(input('n: '))))