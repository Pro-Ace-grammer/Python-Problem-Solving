def tolist(st):    #function to be used to convert comma saperated string to list
    l1 = st.split(',')
    l2 = []
    for i in l1:
        l2+=[int(i)]
    return l2


'''
Program to sort a list in ascending order
Algo:
- first we take an input string of numbers from the use and conver it into a list
- iterate inside this list from i
- then iterate inside the same list again from i+1
- check if l1[j]<l1[i] then perform swapping
- i.e. l1[i],l1[j]=l1[j],l1[i] repeat same for the entire length of the list
- and then return or print the list
'''
# l1 = tolist(input('Enter comma saperated integers: '))
# #in= [4,7,2,3,9]
# #out= [2,3,4,7,9]
# i = 0
# while i < len(l1):
#     j=i+1
#     while j<len(l1):
#         if l1[j]<l1[i]:
#             l1[i],l1[j]=l1[j],l1[i]
#         j+=1
#     i+=1
# print(l1)


# # Below is the same program but to print the list in the descending order
# l1 = tolist(input('Enter comma saperated integers: '))
# #in= [4,7,2,3,9]
# #out= [9,7,4,3,2]
# i = 0
# while i < len(l1):
#     j=i+1
#     while j<len(l1):
#         if l1[j]>l1[i]:
#             l1[i],l1[j]=l1[j],l1[i]
#         j+=1
#     i+=1
# print(l1)

