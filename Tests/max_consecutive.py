'''
To find the longest consecutive sequesnce of the same characters in the input string
'''

def max_consecutive_length(st,i=0,temp='',count=1,max_c=1):
    while i<len(st):
        if st[i] in temp:
            if st[i] == st[i-1]:
                count +=1
                if count>max_c:
                    max_c = count
            else:
                count = 1
        else:
            temp+=st[i]
            count = 1
        i+=1
    return max_c

print(max_consecutive_length(input('str: ')))