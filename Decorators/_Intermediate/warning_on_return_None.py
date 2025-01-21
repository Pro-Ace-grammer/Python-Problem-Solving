'''
Implement a decorator that logs a warning if the return value of a function is None
'''

def warn_if_none(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res is None:
            print('Warning: Function Returned None')
        return res
    return wrapper

@warn_if_none
def hello():
    print('Hello how are you doing?!')

@warn_if_none
def sample(a,b):
    import time
    time.sleep(2)
    return a+b

print(hello())
print(sample(3,5))