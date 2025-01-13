'''
this program moves all the zeros in the list at the end
'''
# def lis(st):
#     l1 = st.split(',')
#     l2 = []
#     for i in l1:
#         l2+=[int(i)]
#     return l2

def move_zero(l):
    l1 = []
    l2 = []
    for i in l:
        if i == 0:
            l2+=[i]
        else:
            l1+=[i]
    return l1+l2


# a = lis(input('Enter comma saperated integers: '))
l = move_zero([0,8,7,6,0,9,0,9,7,1,2,0,0])
print(l)