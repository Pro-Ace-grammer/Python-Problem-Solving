'''
25-september-2023 

Given an integer x, return true if x is a palindrome, and false otherwise.
Without typecasting into String

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1
'''

class Solution(object):
    def isPalindrome(self, x):
        temp,res=x,0
        if x>0:
            while temp>0:
                res =res*10+(temp%10)
                temp//=10
        return x==res
p = Solution()
print(p.isPalindrome(121))

'''
time = 51ms
space = 13.15 mb
'''