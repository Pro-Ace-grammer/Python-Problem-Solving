'''
OOP:
 - This is one of the imnportant concept which is commly used in most of the programming languages
 
 - In OOP we have classes and objects
 - class is a blueprint of an object 
 - object is a real time entity or it is an instance of a class
 '''

# class sample: #we define a class using 'class' keyword and sample is the name of the class
#     pass #inside this class contains the properties/states/members & functionality/behaviour/methods

# s = sample()    #s is an object of class sample
'''
under members or properties or states we have 2 different types 
 - Generic States / class members:
    -   These are the ones that are usuallly written inside a class


 - specific states / object members
    -   these are the members which are specific for particular object
'''
# example of generic states or class memmbers
# class student:
#     course = 'python'   #This is a class member
#     institure = 'PySpiders' #class member
#     code = 'PBT-PFFPTD-A3'  #class member

# s1 = student()  #creating an object
# print(s1.course, s1.institure, s1.code, sep='\n') # calling the class members with the help of object 's1'

# # below is the example of specific state
# # let's create one more object
# s2 = student()  # this object belongs to class student 
# #the above object can also access the class members similar to the prevoious one 
# #now let us create some specific states or object member 
# #Below is how we create object members
# s2.name = 'Arsalan'     # this is an object member which can be accessed only by object 's2'
# s2.phno = 9096597936
# print(s2.name, s2.phno, sep='\n')

# print(s1.name)  #if we try to access the name variable which is a member of object s2 by using s1 then it will throw an error


#let us create a class as bank and make generic states and specific states 
# class bank:
#     #the below variable we see which are written inside a class are all class members or generic states
#     bname = 'SBI'
#     state = 'Goa'
#     branch = 'Pernem'

# p = bank()
# #the below variables we see are all object members of specific states which are only accessible to object p
# p.name = 'Arsalan'
# p.ifsc = 'SBI8376289'
# p.acno = 43785934758



#------------------------ CONSTRUCTOR -------------------------------
'''
 - These are the magic methods which are used to create an object and its members within the class
 - python has three types of constructors
 1. default constructor
 2. parameterized constructor
 3. non - parameterized constructor
'''
#there are many but the one which we care about is the param,eterized constructor i.e. __init__()

#below is an example of using the __init__ method
# class bank:
#     def __init__(self): # this is a method which gets automatically called when the objecr of class is created
#         print('This is __init__')
#         # we do not have to saperately call this method unlike other

# obj = bank()
#as soon as we created the above object of class bank, the __init__ method got called and the block of code residing inside the class was executed


#similar to __init__ there is one more method called as __new__
#this is also a method which is used as a default constructor to create an object for particular class.
#this executes automatically to support the object creation
#it is an empty method which just support in object creation withou any function call.
#below is the example for the same 
# class new:
#     def __new__(self):
#         print('The object is created!!')

# obj = new() # as soon as we create this object the __new__ method is called


#different ways to pass the arguments to the class
#normal argument passing through parameters
# class exp:
#     def __init__(self, a, b):
#         self.name = a
#         self.phno = b
#         self.disp()

#     def disp(self):
#         print(self.name)
#         print(self.phno)

# ex1 = exp('Arsalan',8389734783)
# ex2 = exp(input('name: '),int(input('phno: ')))


#wihtout passing through argument
# class exp:
#     def __init__(self):
#         self.name = input('name: ')
#         self.phno = int(input('phno: '))
#         self.disp()

#     def disp(self):
#         print(self.name)
#         print(self.phno)

# p = exp()
