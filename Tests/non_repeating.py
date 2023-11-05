'''
to find single non repeating number
'''

def non_rep(l,c=0,t = []):
    for i in l:
        for j in l:
            if i == j:
                c+=1
        if c == 1:
            t += [i]
        else:
            c=0
    return t

    
print(non_rep([2,3,1,1,4,2,9,4,2,6,6]))
