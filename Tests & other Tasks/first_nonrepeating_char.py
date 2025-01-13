'''
This program finds the first non repeating character in the string and returns its index
'''

def non_repeat(st):
    count = 0
    for i in range(len(st)):
        for j in st:
            if count == 1 and j == st[-1] and st[i]!=j:
                return i
            if st[i]==j:
                count+=1
        count=0

ind = non_repeat(input('Enter a string: '))
print(ind)