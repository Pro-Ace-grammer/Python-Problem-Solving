# Find maximum in the list.
def max_num(l,max=-9999):
    if not l:
        return max
    elif max<l[0]:
        return max_num(l[1:],max=l[0])
    return max_num(l[1:],max)
    
print(max_num([3,4,6,768,1,87,34,634,87]))