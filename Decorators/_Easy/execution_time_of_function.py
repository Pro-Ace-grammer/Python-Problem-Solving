'''
Create a decorator that calculates the execution time of a function.
'''

import time

def timer(func):
    def inner(*args, **kwargs):
        st = time.time()
        res = func(*args,**kwargs)
        end = time.time()
        print(f'Time taken to execute {func.__name__}() was {end-st}')
        return res
    return inner

@timer
def sample(a,b):
    time.sleep(2)
    return a+b

print(sample(6,4))