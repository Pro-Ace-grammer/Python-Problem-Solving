# def first_non_repeating(st):
#     hashmap = {}
#     for i in range(len(st)):
#         char = st[i]
#         if char in hashmap:
#             hashmap[char] = (hashmap[char][0]+1,i)
#         else:
#             hashmap[char] = (1,i)
#     for val in hashmap.values():
#         if val[0] == 0:
#             return val[1]
#     return -1


def first_non_repeating(st):
    hashmap = {}
    for char in st:
        if char in hashmap:
            hashmap[char] = hashmap[char]+1
        else:
            hashmap[char] = 1
    for key,val in enumerate(st):
        if hashmap[val] == 1:
            return key
    return -1


#Shorter version of the condition
def first_non_repeating(st):
    hashmap = {}
    for char in st:
        hashmap[char] = hashmap.get(char,0)+1\
        
    for key,val in enumerate(st):
        if hashmap[val] == 1:
            return key
    return -1
# st = "lleetcode"
# print(first_non_repeating(st))


st = "arsalan"
print(first_non_repeating(st))