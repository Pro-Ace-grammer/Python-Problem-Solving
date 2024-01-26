'''
find the sum of all th integers in the below list
'''



def sum_int(lis,res=0,i=0):
    if i<len(lis):
        if type(lis[i]) == int:
            res+=lis[i]
        elif type(lis[i]) in (list,tuple):
            res+= sum_int(lis[i])
        return sum_int(lis,res,i+1)
    return res


lis = [2,3,4,5,'str',3+8j,[1,2,4,'hii'],(10,20),['str',4,3,['yo',2,3,True,(5,2)]]]
print(sum_int(lis))