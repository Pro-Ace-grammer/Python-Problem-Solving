'''
Write a Python function that finds the maximum sum of a contiguous subarray within a given list of integers. The subarray can contain both positive and negative numbers.

For example, given the list [1, -2, 3, 4, -1, 2, 1, -5, 4], the maximum subarray sum is 6, which corresponds to the subarray [3, 4, -1, 2, 1].

Your function should take the list of integers as input and return the maximum subarray sum.
'''

def max_sum(l1):
    c_sum=0
    m_sum=0
    for i in l1:
        c_sum+=i
        m_sum=max(c_sum,m_sum)
        if c_sum<0:
            c_sum=0
    return m_sum


print(max_sum([1, -2, 3, 4, -1, 2, 4]))
