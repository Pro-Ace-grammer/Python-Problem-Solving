'''
Advanced Questions
Create a decorator factory (a decorator that takes arguments) to prepend a specific string to the output of a function.


Write a decorator that enables a function to log all its execution details to a file.
'''

def prepend_string(prepend_text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            result = func(*args, **kwargs)
            return f'{prepend_text} {result}'
        return wrapper
    return decorator

@prepend_string('From Code Ace')
def greet(msg):
    return msg

print(greet('Helloo World'))