'''
Python program to interchange the first and the last element of the list
'''

def lis(st):
    l1 = st.split(',')
    l2 = []
    for i in l1:
        l2+=[int(i)]
    return l2

# def interchange(l1):
#     l1[0],l1[-1] = l1[-1],l1[0]
#     return l1

# l1 = lis(input('Enter comma saperated integer: '))
# a = interchange(l1)
# print(a)




'''
Python program to swap two elements in a list
'''

def swap(l1, pos1, pos2):
    l1[pos1],l1[pos2] = l1[pos2],l1[pos1]
    return l1

l1 = lis(input('Enter comma saperated integer: '))
a = swap(l1,int(input('1st position'))-1,int(input('2nd position'))-1)
print(a)