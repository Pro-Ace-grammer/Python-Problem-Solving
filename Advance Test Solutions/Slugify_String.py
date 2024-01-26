'''
Write a python function to generate a slug from a gien string. A slug is a URL friendly
version of a string

The function should perform the following
1. Convert the string to lowercase
2. Replace spaces with hyphens (-)
3. Remove any special characters (except hyphens) and puncuations
4. Ensure the slug doensn't start or end with a hyphen
5. If multiple hyphens appear consecutively, replace them with a single hyphen.

example
string = '  Hello!!   How are you doing??!! '

output = 'hello-how-are-you-doing'
'''

def slugify(st):
    res=''
    for ch in st.strip():
        if 'A'<=ch<='Z':
            res+=chr(ord(ch)+32)
        elif 'a'<=ch<='z':
            res+=ch
        elif ch == " " and res[-1]!='-':
            res+='-'
    return res

st = '  Hello world!!    How are you doing today...  '
print(slugify(st))
        
