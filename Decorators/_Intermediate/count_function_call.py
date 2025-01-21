'''
Create a decorator that keeps track of how many times a function has been called.
'''

def track_call(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        inner.count += 1    
        print(f'Function was called {inner.count} time(s)')
    inner.count = 0 # initializing an attribute for inner function or wrapper.
    return inner

@track_call
def hello():
    print('Hello how are you')

hello()
hello()
hello()
hello()




# def call_counter(func):
#     def wrapper(*args, **kwargs):
#         wrapper.call_count += 1
#         print(f"{func.__name__} has been called {wrapper.call_count} times.")
#         return func(*args, **kwargs)
#     wrapper.call_count = 0
#     return wrapper

# @call_counter
# def example_function():
#     print("Function is running.")