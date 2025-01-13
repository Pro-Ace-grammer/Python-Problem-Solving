'''
Python function to check whether the given number is perfect or not

if the sum of the factors of the number is equal to the number then the number is perfect number
'''
def perfect(n):
    sum = 0
    for i in range(1, (n+1)//2):
        if n%i ==0 :
            sum+=i
    if sum == n:
        print(True)
    else:
        print(False)

perfect(int(input('n: ')))