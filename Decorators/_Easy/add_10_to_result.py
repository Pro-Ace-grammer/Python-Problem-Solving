'''
Create a Decorator that adds 10 to the result of any function it wraps
'''

def add_10(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return res+10
    return inner


@add_10
def summation(*args):
    from functools import reduce
    x = lambda n,m:n+m
    res = reduce(x,[arg for arg in args])
    return res


print(summation(1,2,3,4,5))