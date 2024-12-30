# Example 3: Sum of Digits.
def digitSum(num):
    if num==0:
        return 0
    else:
        return (num%10)+digitSum(num//10)

print(digitSum(12345))

