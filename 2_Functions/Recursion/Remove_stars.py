'''
input = 'python**abc*
output = 'pythab'
'''

def mod_str(st,res='',i=0):
    if i <len(st):
        if st[i]=='*':
            res = res[:-1]
        else:
            res+=st[i]
        return mod_str(st,res,i+1)
    return res

print(mod_str(input()))