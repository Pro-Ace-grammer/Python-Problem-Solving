'''
to remove duplicates from the array
'''

def rem_duplicate(nums):
    i=0
    c=1
    while i<len(nums):
        j=0
        while j<len(nums):
            if nums[i] == nums[j]:
                nums = nums[:j]+nums[j+1:]
                c+=1
            j+=1
        i+=1
    return nums+['_']*c

print(rem_duplicate([1,1,2,3,3,4,5]))


##nums = [1,1,2]
##nums = nums[:1]+nums[2:]
##print(nums)

