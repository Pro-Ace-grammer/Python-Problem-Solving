'''
Given number N, the task is to check whether it is fascinating or not...

Fascinating Number: When a number(3 digits or more) is multiplied by 2 and 3 and
when both these products are concatenated with the original number, then it results
in all digits from 1 to 9 present exactly once. These could be any number of zeros
and are ignored

'''

def num_count(nums):
    for i in range(1,10):
        c = 0
        for ch in nums:
            if str(i)==ch:
                c+=1
        if c >1 or c<1:
            return False
    return True
    

def is_fascinating(n):
    try:
        prod2 = int(n)*2
        prod3 = int(n)*3
        res_concat = str(prod2)+str(prod3)+n
        print(f'concatenating {n}+{prod2}+{prod3}=',res_concat)
        if num_count(res_concat):
            print('Fascinating number')
        else:
            print('Not Fascinating Number')
    except ValueError:
        print("ValueError: Make sure to enter a number")


n = input('Enter a number: ')
is_fascinating(n)
