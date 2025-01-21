'''
Write a decorator that modifies a function to return its output in uppercase.
'''

def to_upper(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return res.upper()
    return inner

@to_upper
def concat(st1,st2):
    return st1+' '+st2

@to_upper
def remove_vowels(st):
    temp = ''.join(ch for ch in st if ch not in 'aeiouAEIOU')
    return temp

print(concat('Hello', 'How are you'))
print(remove_vowels('Hello'))