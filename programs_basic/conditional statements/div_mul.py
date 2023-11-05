"""This program finds those numbers which are divisible by 7 and multiples of 5 between 1500 and 2700 (both included)"""
number_list = []    #this will store the numbers in a list
# for i in range(1500,2701):
#     if i%7==0 and i%5==0:
#         number_list.append(i)
# print(number_list)


#Same program using while loop
i = 1500
while i <= 2700:
    if i%7==0 and i%5==0:
        number_list.append(i)
    i+=1
print(number_list, len(number_list), sep='\n')
# Just for my reference i am prining also the number of elements 