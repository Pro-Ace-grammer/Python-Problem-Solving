# d1={'(':')','{':'}','[':']'}
# val = '{'
# print(d1[val])

list1 = [1,3,4]
list2 = [1,2,5]
res_list = []
l = len(list1)
for i in range(0,l):
    if list1[i]<list2[i]:
        res_list += [list1[i]] + [list2[i]]
    if list1[i]>list2[i]:
        res_list+= [list2[i]] + [list1[i]]
    if list1[i] == list2[i]:
        res_list += [list1[i]] + [list2[i]]

print(res_list)