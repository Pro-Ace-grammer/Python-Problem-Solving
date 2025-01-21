'''
Write a decorator that logs the name of a function and its arguments every time it is called.
'''

def log_it(func):
    def inner(*args, **kwargs):
        arg_values = ', '.join(str(arg) for arg in args)
        kwarg_values = ', '.join(f'{k}={v}' for k,v in kwargs.items())
        print(f"Calling function '{func.__name__}()'")
        # print(f"Calling function '{func.__name__}({arg_values},{kwarg_values})'")
        print(f"Taking args: {arg_values}")
        print(f"Taking kwargs: {kwarg_values}")
        res = func(*args, **kwargs)
        return res
    return inner

@log_it
def add(a,b,c,d,pi=3.14,g=9.8):
    return (a+b+c+d) * pi * 9.8

add(4,5,6,7, pi=3.149764,g=9.83)