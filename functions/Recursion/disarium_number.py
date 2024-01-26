'''
write recursive function to check if number disarium of not
'''

def disarium(n,res=0,i=0):
    if i<len(n):
        res+= int(n[i])**(i+1)
        return disarium(n,res,i+1)
    return res==int(n)

print(disarium(input()))