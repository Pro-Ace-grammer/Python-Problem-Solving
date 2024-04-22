'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

# Below is my first solution which worked for 115 cases but it could not get a correct output for the given case as argument below
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         s = ''
#         temp = ''
#         if len(strs)==1:
#             return strs[0]
#         for i in range(len(strs)-1):
#             for j in strs[i+1]:
#                 if j in strs[i]:
#                     temp+=j
#                     if (i==0 and temp not in strs[i]) or (i!=0 and temp not in s):
#                         temp = temp[:-1]
#                         break 
#             s = temp
#             temp = ''
#         return s


class Solution:
    def longestCommonPrefix(self, strs):
        # longet common prefix
        lcp = ''
        if strs is None or len(strs)==0:
            return lcp # returning empty string since there is an emepty input
        elif len(strs)==1:
            return strs[0] #returning the first element since
        min_len = len(strs[0]) #taking the length of the first element
        for l in range(1,len(strs)):
            min_len = min(min_len,len(strs[l])) #comparing the lenght and storing the minimu n length
        for i in range (0,min_len):      #checking the elements first - (min_len)th character
            curr = strs[0][i]            #current ith character of first element
            for j in range(1,len(strs)): #iterating to each element
                if strs[j][i] != curr:   #comparing the ith element of each element if equal or not
                    return lcp
            lcp+=curr
        return lcp

cp = Solution()
print(cp.longestCommonPrefix(["reflower","flow","flight"]))
# temp = 'f
# ["flower","flow","flight"]