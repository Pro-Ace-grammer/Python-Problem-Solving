'''
to convert a given string into a list without using any inbuilt function
example 1:
st = python programmin language
output = ['python','programmin','language']

example 2:
st = 1 2 3 4 5 6
output = [1,2,3,4,5,6]
'''


#Error Handling function
def isnum(st):
    flag = True
    try:
        int(st)
    except ValueError:
        flag = False
    return flag


def toList(st):
    l1 = []
    temp = ''
    for i in st:
        if i != ' ':
            temp += i
        else:
            if isnum(temp): 
                l1.append(int(temp))
                temp = ''
            else:
                l1.append(temp)
                temp = ''
    if isnum(temp):
        l1.append(int(temp))
        temp = ''
    else:
        l1.append(temp)
        temp = ''
    return l1
 
l1 = toList(input('string: '))
print(l1)


