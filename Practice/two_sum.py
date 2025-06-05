# Brute force
# the solution has T.C. = O(n^2)
def two_sum(arr,n,target)->list:
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return [i,j]
    return [-1,-1]  

# using hashing
# to return only unique pairs
# This solution has time complexity of O(N)
def two_sum(arr,n,target)->list:
    hashmap = {}
    out = set()
    for i in range(n):
        if target-arr[i] in hashmap:
            out.add(tuple(sorted([target-arr[i],arr[i]])))
        else:
            hashmap[arr[i]] = i
    return list(out)
    
arr = [1, 2, 3, 4, 3]
target = 6
print(two_sum(arr,len(arr),target))