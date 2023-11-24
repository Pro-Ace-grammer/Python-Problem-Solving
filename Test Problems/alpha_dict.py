
def dic(st):
    d1 = {}
    for i in st:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    return d1
d = dic(input('str: '))
print(d)
