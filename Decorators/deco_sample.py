def deco(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper

