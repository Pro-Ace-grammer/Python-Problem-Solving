'''
Write a Python program that defines two functions:

square(x) which returns the square of a number x.
double(x) which returns twice the value of x.
Then, write a third function compose(f, g, x) that takes two functions f and g, and an input value x, and returns f(g(x)).

In other words, the compose function should apply g to x, and then apply f to the result of g(x).
'''

def square(x):
    return x*x

def double(x):
    return x*2

def compose(x):
    return square(double(x))

print(compose(int(input('n: '))))
