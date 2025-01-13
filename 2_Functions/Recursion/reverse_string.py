# Example 6: Reverse a string
def reverse(st):
    if st == '':
        return st
    else:
        return st[-1]+reverse(st[:-1])
    
print(reverse('Hello'))