'''
Python Program to determine whether the given number is perfect or not
'''
def perfect(n,s1=0,i=1):
    if s1<n:
        if n%i ==0:
            s1+=i
        return perfect(n,s1,i+1)
    if s1 == n:
        return 'Perfect'
    else:
        return 'Not Perfect'

n = int(input('enter the number: '))
print(perfect(n))
