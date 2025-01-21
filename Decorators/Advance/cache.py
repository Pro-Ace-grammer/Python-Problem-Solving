def caching(func):
    cache_value = {}
    def inner(*args):
        if args in cache_value:
            return cache_value[args]
        res = func(*args)
        cache_value[args] = res
        return res
    return inner


@caching
def add(a,b):
    import time
    time.sleep(2)
    return a+b

print(add(54,46))
print(add(6,4))
print(add(54,46))