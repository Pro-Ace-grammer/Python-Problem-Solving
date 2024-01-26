'''
Python program that takes a series of integers as user input until as empty line,
saves them to "number.txt", reads the file to calculate the sum of integers,and prints the result

example:
number.txt
5
10
-3
8
output - 20
'''

with open("numbers.txt","w") as f:
    while True:
        n = input('Enter a number: ')
        if n is None or n == '':
            break
        else:
            f.writelines(n+'\n')

with open("numbers.txt","r") as f:
    a = f.readlines()
    res = 0
    for i in a:
        res += int(i)

print(f'sum = {res}')

