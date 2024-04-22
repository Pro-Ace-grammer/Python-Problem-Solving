'''
25-september-2023

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

'''

class Solution:
    def romanToInt(self,s):
        d1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sumInt = 0 #to store integer equivalent of the given roman number string
        i=0
        while i<len(s):
            #below condition is to check whether the integer equivalent is 4,9,40,90,400, or 900
            if (i!=len(s)-1) and ((s[i]=='I' and s[i+1] in 'VX') or (s[i]=='X' and s[i+1] in 'LC') or (s[i]=='C' and s[i+1] in 'DM')):
                    sumInt += d1[s[i+1]]-d1[s[i]]
                    i+=2
            else:
                sumInt+= d1[s[i]]
                i+=1
        return sumInt

rom = Solution()
print(rom.romanToInt(input('Enter Roman Number: ').upper()))

'''
time: 36ms
memory: 13.30 mb
'''