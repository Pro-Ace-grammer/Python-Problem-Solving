'''
this program returns true if any one of the element in two lists is common
'''
def tolist(st):
    l1 = st.split(',')
    l2 = []
    for i in l1:
        l2+=[int(i)]
    return l2


def common(l1,l2):
    for i in l1:
        for j in l2:
            if i == j:
                return True,i
            
l1 = tolist(input('Enter comma saperated integers: '))
l2 = tolist(input('Enter comma saperated integers: '))
print(common(l1,l2))


# same function using while 
# def common(l1,l2):
#     i = 0
#     while i < len(l1):
#         j = 0
#         while j<len(l2):
#             if l1[i]==l2[j]:
#                 return True, l1[i]
#             j+=1
#         i+=1
