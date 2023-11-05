'''
python function to rempve the nth index from the given string and return a new string
'''

def st_remove(st,n):
    last_st = st[:n-1] + st[n:]
    return last_st

st = input('Enter the string: ')
n = int(input('Enter the index of the character you want to remove: '))
print(st_remove(st,n))