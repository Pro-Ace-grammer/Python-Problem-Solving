'''
to implement the stack operations on lists
'''
def push(l1,el):
    l1 += [el]
    return l1

def pop(l1):
    l1=l1[:-1]
    return l1

def display(l1):
    print('\n',l1)

l1 = []
while True:
    print('''
    1. PUSH     2. POP
    3. Display  4. Exit''')
    n = int(input('Enter your choice: '))
    if n ==1:
        l1 = push(l1,int(input('Enter the element you want to add: ')))
    elif n ==2:
        l1 = pop(l1)
    elif n==3:
        display(l1)
    elif n == 4:
        break
    else:
        print('invalid input')