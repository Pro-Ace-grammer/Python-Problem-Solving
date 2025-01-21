'''
Write a decorator that allows a function to be retried up to 3 times in case of an exception.
'''

def retry_on_exception(tries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1,tries+1):
                try:
                    result = func(*args,**kwargs)
                    return result
                except Exception as e:
                    print(f'Attemt {attempt} fail with error: {e}')
                    if attempt == tries:
                        return 'Task Failed: No More attemps Left'
        return wrapper
    return decorator


@retry_on_exception(tries=3)
def risky_function(n):
    if n<0:
        raise ValueError("Negative value not allowed")
    return f"Success with value {n}"

print(risky_function(5))
print(risky_function(-9))