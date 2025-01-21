# def outer():
#     print('Outer running')
#     def inner():
#         print('Inner running')
#         def innermost():
#             print('innermost running')
#             return 'Hello'
#         return innermost
#     return inner


# print(outer()) # this will only run the outer function and return inner address
# print(outer()()) # this will run both outer and inner and return innermost address
# print(outer()()()) # this will run all the functions and return hello





def outer(a,b):
    print(a,b)
    def inner(func):
        print('Inner running')
        def innermost(*args):
            print('innermost running')
            func(*args)
            return 'Hello'
        return innermost
    return inner


@outer(a=3,b=8)
def sam(p,q,r):
    print(p,q,r)
    print('done executing')
print(sam(22,55,99))


# So the simplest way to look at the above function call with a decorator is
def sam(p,q,r):
    print(p,q,r)
    print('done executing')
outer(a=3,b=8)(sam)(22,55,99)
# here the params in first parantheses are for the outer function 
# the second paranthese args are for the inner function ...
# third args are for the innermost function which is wrapping the original function...