'''
This program takes a list of numbers as input and returns a new list. In the new list, the i-th element will be equal to the sum of the first i(i+1) elements in the input list
input: [1,2,4,6,3,2]
output: [1,3,7,13,15,17]
'''
def lis(st):
    l1 = st.split(',')
    l2 = []
    for i in l1:
        l2+=[int(i)]
    return l2

def sum_list(l1):
    j = 0
    l2 = []
    for i in l1:
        l2 += [j+i]
        j = j+i
    print(l2)

a = lis(input('Enter comma saperated numbers: '))
sum_list(a)

# st = input('enter: ')
# l1 = st.split(',')
# print(l1)
# print(int(l1[1]))