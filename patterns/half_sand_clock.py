'''
* * * *
* * *
* *
*
* *
* * *
* * * *
'''
n = int(input())
'''
temp = n
for i in range(0,n):
    print('* '*temp)
    temp-=1
temp=2
for j in range(0,n-1):
    print('* '*temp)
    temp+=1
''' 



'''

*
* *
* * *
* * * *
* * * *
* * *
* *
*

'''
temp =1
for a in range(1,11):
    for j in range(0,n):
        print('* '*temp)
        temp+=1
    temp = n-1
    for i in range(0,n-1):
        print('* '*temp)
        temp-=1
