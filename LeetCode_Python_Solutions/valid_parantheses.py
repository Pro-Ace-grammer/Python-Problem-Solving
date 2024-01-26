'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

#Below is my starting attempt to solve the program which then I had to cancel since it could not work for some specific cases so had to come up with some other solution to this problem
# class Solution(object):
#     def isValid(self, s):
#         flag = False
#         if s is None or len(s) in(0,1) or len(s)%2!=0 or s[0] in '}])' or s[len(s)-1] in'([{':
#             return False
#         for i in range(len(s)): 
#             if (i!=len(s)-1):
#                 if (s[i] == '(' and s[i+1]==')') or (s[i] == '[' and s[i+1]==']') or (s[i] == '{' and s[i+1]=='}'): 
#                     flag =True
#                     i+=2
#                 elif (s[i] == '(' and s[len(s)-(i+1)]==')') or (s[i] == '[' and s[len(s)-(i+1)]==']') or (s[i] == '{' and s[len(s)-(i+1)]=='}'):  
#                     flag =True
#                     i+=1    
#                 else:
#                     flag = True
#             else:
#                 return flag     
#         return flag          

# par = Solution()
# print(par.isValid('(()())]]'))




#So what we can do is we can use the stack operations to perform the same
# so whenever we get a opening we can push it in our stack and as soon as we find a closing we check if the closing bracket have its corresponding opening bracket or not
#if it is true then we will check if the last added element is its opening or not 
#if it is then we would directly pop the last element from the stack and carry forward else return false directly

#[(){([])}]

class Solution:
    def isValid(self,s):
        stack = ''  
        d1={')':'(','}':'{',']':'['}
        if s is None or len(s) in(0,1) or len(s)%2!=0 or s[0] in '}])' or s[len(s)-1] in'([{':
            return False
        for k,val in enumerate(s):
            key = val
            if val in '({[':
                stack += val
            elif val in '}])' and stack != '' and stack[-1] == d1[key]:
                stack = stack[:-1]
            else:
                return False
        if stack == '':
           return True
        else:
            return False

valid = Solution()
print(valid.isValid('()))'))           
'''('''
'''(()([]))''' 
    