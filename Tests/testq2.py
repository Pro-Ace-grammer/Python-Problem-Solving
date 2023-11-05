x = 'abcddcba'
temp = ''
for i in x:
    if i in temp:
        print(i)
        break
    else:
        temp = temp + i
        
 
