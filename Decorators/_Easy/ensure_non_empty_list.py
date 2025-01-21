'''
Implement a decorator that ensures the wrapped function is only called if it's passed a non-empty list
'''

def deco(func):
    def inner(arg):
        if type(arg) == list and arg:
            func(arg)
        else:
            print('Function not called: Argument must be a non-empty list!!')
    return inner


@deco
def process_list(lst):
    print('Processing the List!!')


process_list([3,4,6])
process_list((3,4,6))
process_list([])