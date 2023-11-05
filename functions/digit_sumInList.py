'''
python program to find sum of digits of a number in a list
example:
in = [12,23,43,66]
ot = [3,5,7,12]
'''


def lis(st):
    l1 = st.split(',')
    l2 = []
    for i in l1:
        l2+=[int(i)]
    return l2

def sum_dig(l1):
    l2 = []
    for i in l1:
        sum = 0
        for j in str(i):
            sum+=int(j)
        l2.append(sum)
    return l2

l1 = lis(input('Enter comma saperated integer: '))
a = sum_dig(l1)
print(a)