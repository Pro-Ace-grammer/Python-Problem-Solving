'''
Recursion is basically a function calling itself again and again several number of times until the base condition is reached.

Key Points about Recursion:
Base Case: Every recursive function needs a base case that will stop the recursion. Without it, the function will call itself indefinitely, leading to a stack overflow.

Recursive Case: This is where the function calls itself with a modified argument, gradually moving towards the base case.
'''

#Example 1: Factorial of a number
# def facto(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return num*facto(num-1)

# print(facto(5))


# Find maximum in the list.
def max_num(l,max=-9999):
    if not l:
        return max
    elif max<l[0]:
        return max_num(l[1:],max=l[0])
    return max_num(l[1:],max)
    
print(max_num([3,4,6,768,1,87,34,634,87]))