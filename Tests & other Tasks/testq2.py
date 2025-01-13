'''
Program to remove duplicates from a string
'''
x = 'abbcdcbba'
temp = ''
for i in x:
    if i in temp:
        continue
    else:
        temp = temp + i
        
print(temp)
