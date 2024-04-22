'''
Program to merge two sorted linked lists
'''

from Linked_List import LinkedList

LL1 = LinkedList()
LL1.insert(1)
LL1.insert(3)
LL1.insert(4)

LL2 = LinkedList()
LL2.insert(1)
LL2.insert(2)
LL2.insert(5)

# l = LL1.length() if LL1.length() > LL2.length() else LL2.length()

# ptr1 = LL1.head
# ptr2 = LL2.head
# res = LinkedList()
# while ptr1:
#     if ptr1.data < ptr2.data or ptr1.data == ptr2.data:
#         res.insert(ptr1.data)
#         res.insert(ptr2.data)
#     if ptr1.data > ptr2.data:
#         res.insert(ptr2.data)
#         res.insert(ptr1.data)
#     ptr1 = ptr1.next
#     ptr2 = ptr2.next

# res.printLL()



# SOLUTION 2

def merge_list(list1, list2, cur):
    if not list1 or not list2:
        return list1 if list1 else list2
    
    if list1.data < list2.data:
        list1.next = merge_list(list1.next, list2)
        list1.data
        print(list1,'\n\n')
    else:
        list2.next = merge_list(list1,list2.next)
        print(list2,'\n\n')
    

merge_list(LL1,LL2,LL1.head)
