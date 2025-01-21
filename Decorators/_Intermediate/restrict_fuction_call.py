'''
A decorator that restricts a function from being called more than 3 times.
'''

def restrict(func):
    def wrapper(*args, **kwargs):
        if wrapper.count < 3:
            res = func(*args, **kwargs)
            wrapper.count += 1
        else:
            print('Function cannot be called more than 3 times!!')
    wrapper.count = 0
    return wrapper


@restrict
def hello():
    print('Hello how are you doing?!')


hello()
hello()
hello()
hello()