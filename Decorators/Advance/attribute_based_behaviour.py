'''
How would you write a decorator that applies different behaviors to functions based on their metadata (e.g., a custom attribute set on the function)?
'''

from functools import wraps

def attribute_based_behaviour(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Accessing the 'behavior' attribute using getattr
        # behavior = getattr(wrapper, 'behavior', None)
        # print(f"Function: {func.__name__}, Behavior: {behavior}")
        result = func(*args, **kwargs)
        
        if wrapper.behavior == 'uppercase':
            return result.upper()
        elif wrapper.behavior == 'reverse':
            return result[::-1]
        return result
    
    # Copy the 'behavior' attribute to the wrapper
    wrapper.behavior = getattr(func, 'behavior', None)
    return wrapper

@attribute_based_behaviour
def greet(name, text):
    return f"Hello {name}, {text}"
greet.behavior = 'uppercase'  # Assign behavior to the wrapper

@attribute_based_behaviour
def reverse(message):
    return message
reverse.behavior = 'reverse'  # Assign behavior to the wrapper

# Test the functions
print(greet('People', 'How you all are doing?'))
print(reverse('Love Laugh Live'))


# from functools import wraps

# def attribute_based_behaviour(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         result = func(*args, **kwargs)
#         if hasattr(func, 'behavior'):
#             if func.behavior == 'uppercase':
#                 return result.upper()
#             elif func.behavior == 'reverse':
#                 return result[::-1]
#             else:
#                 return result
#         else:
#             return result
#     return wrapper

# @attribute_based_behaviour
# def greet(name, text):
#     return f"Hello {name}, {text}"
# greet.behavior = 'uppercase'

# @attribute_based_behaviour
# def reverse(message):
#     return message
# reverse.behavior = 'reverse'

# print(greet('People', 'How you all are doing?'))
# print(reverse('Love Laugh Live'))

# # Convert bytes to KB and MB
# import sys
# size_in_bytes = sys.getsizeof("Hello, world!   hri fguiasbui bsuipbuipbsfug bsfibguiogs")
# size_in_kb = size_in_bytes / 1024  # 1 KB = 1024 bytes
# size_in_mb = size_in_kb / 1024     # 1 MB = 1024 KB

# print(f"Size in bytes: {size_in_bytes}, in KB: {size_in_kb:.2f}, in MB: {size_in_mb:.4f}")
