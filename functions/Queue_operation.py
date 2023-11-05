'''
to implement the Queue operations on list
'''
def insert(l1,el):
    l1 += [el]
    return l1


def delete(l1):
    l1=l1[1:]
    return l1

def display(l1):
    print('\n',l1)


l1 = []
while True:
    print('''
    1. Insert   2. Delete
    3. Display  4. Exit''')
    n = int(input('Enter your choice: '))
    if n ==1:
        l1 = insert(l1,int(input('Enter the element you want to add: ')))
    elif n ==2:
        l1 = delete(l1)
    elif n==3:
        display(l1)
    elif n == 4:
        break
    else:
        print('invalid input')