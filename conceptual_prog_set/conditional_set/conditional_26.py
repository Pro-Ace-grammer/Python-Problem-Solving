'''
1. Write a C program to accept two integers and check whether they are equal or not.
Test Data : 15 15
Expected Output :
Number1 and Number2 are equal
'''
# a = int(input('a: '))
# b = int(input('b: '))
# if a == b:
#     print('a and b is equal')
# else:
#     print('a and b is not equal')


'''
2. Write a C program to check whether a given number is even or odd.
Test Data : 15
Expected Output :
15 is an odd integer
'''
# n= int(input('Enter a number: '))
# if n%2==0:
#     print(n,'is an even number')
# else:
#     print(n,'is an odd number')

'''
3. Write a C program to check whether a given number is positive or negative.
Test Data : 15
Expected Output :
15 is a positive number
'''
# n= int(input('Enter number: '))
# if n<0:
#     print(n,'is a negataive number')
# else:
#     print(n,'is a positive number')

'''
4. Write a C program to find whether a given year is a leap year or not.
Test Data : 2016
Expected Output :
2016 is a leap year.
'''
# year = int(input('Enter the year: '))
# if year%100!=0:
#     if year%4==0:
#         print(year,'is a leap year')
#     else:
#         print(year,'is not a leap year')
# elif year%400==0:
#     print(year,'is a leap year')
# else:
#     print(year,'is not a leap year')


'''
5. Write a C program to read the age of a candidate and determine whether he is eligible to cast his/her own vote.
Test Data : 21
Expected Output :
Congratulation! You are eligible for casting your vote.
'''
# age = int(input('Enter your age'))
# if age>=18:
#     print('You are eligible to vote')
# else:
#     print('Your are not eligible to vote ')


'''
6. Write a C program to read the value of an integer m and display the value of n is 1 when m is larger than 0, 0 when m is 0 and -1 when m is less than 0.
Test Data : -5
Expected Output :
The value of n = -1
'''
# m = int(input('Enter a number'))
# if m>0:
#     print('The value of n = 1')
# elif m==0:
#     print('The value of n = 0')
# else:
#     print('The value of n = -1')


'''
7. Write a C program to accept the height of a person in centimeters and categorize the person according to their height.
Test Data : 135
Expected Output :
The person is Dwarf.
'''
# h = int(input('Enter your Height: '))
# if h<=135:
#     print('the person is Short')
# else:
#     print('The person is Tall')

'''
8. Write a C program to find the largest of three numbers.
Test Data : 12 25 52
Expected Output :
1st Number = 12,        2nd Number = 25,        3rd Number = 52
The 3rd Number is the greatest among three
'''
# a=int(input('a: '))
# b=int(input('b: '))
# c=int(input('c: '))
# if a>b:
#     if a>c:
#         print('A is Largest')
#     else:
#         print('C is Largest')
# else:
#     if b>c:
#         print('B is largest')
#     else:
#         print('C is largest')


'''
9. Write a C program to accept a coordinate point in an XY coordinate system and determine in which quadrant the coordinate point lies.
Test Data : 7 9
Expected Output :
The coordinate point (7,9) lies in the First quadrant.
'''
# x = int(input('x: '))
# y = int(input('y: '))
# if x >=0 and y >= 0:
#     print(f'The coordinate point {x,y} lies in the First quadrant.')
# elif x<=0 and y>=0:
#     print(f'The coordinate point {x,y} lies in the Second quadrant.')
# elif x<=0 and y <=0:
#     print(f'The coordinate point {x,y} lies in the Third quadrant.')
# elif x>=0 and y <=0:
#     print(f'The coordinate point {x,y} lies in the Fourth quadrant.')


'''
10. Write a C program to determine eligibility for admission to a professional course based on the following criteria: Go to the editor
Eligibility Criteria : Marks in Maths >=65 and Marks in Phy >=55 and Marks in Chem>=50 and Total in all three subject >=190 or Total in Maths and Physics >=140 ------------------------------------- Input the marks obtained in Physics :65 Input the marks obtained in Chemistry :51 Input the marks obtained in Mathematics :72 Total marks of Maths, Physics and Chemistry : 188 Total marks of Maths and Physics : 137 The candidate is not eligible.
Expected Output :
The candidate is not eligible for admission.
'''
# m = int(input('Enter marks for Math: '))
# p = int(input('Enter marks for Physics: '))
# c = int(input('Enter marks for Chemistry: '))
# print('Marks in PCM = ',p+c+m)
# print('Marks in p+m: ',p+m)
# if m>=65 and p>=55 and c>=50:
#     if p+c+m >=190 or m+p>=140:
#         print('The candidate is eligible for admission')
#     else:
#         print('The candidate is not eligible for admission')
# else:
#     print('The candidate is not eligible for admission')


'''
11. Write a C program to calculate the root of a quadratic equation.
Test Data : 1 5 7
Expected Output :
Root are imaginary;
No solution.
'''
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# d = b*b - (4*a*c)

# if d == 0:
#     x1 = -b / 2*a*c
#     x2 = x1
#     print('The roots are : ',round(x1,2),round(x2,2))
# elif d>0:
#     x1 = (-b+d) / (2*a*c)
#     x2 = (-b-d) / (2*a*c)
#     print('The roots are : ',round(x1,2),round(x2,2))
# else:
#     print('The roots are Imaginary, hence the equation have no solution')

'''
2. Write a C program to read the roll no, name and marks of three subjects and calculate the total, percentage and division.
Test Data :
Input the Roll Number of the student :784
Input the Name of the Student :James
Input the marks of Physics, Chemistry and Computer Application : 70 80 90
Expected Output :
Roll No : 784
Name of Student : James
Marks in Physics : 70
Marks in Chemistry : 80
Marks in Computer Application : 90
Total Marks = 240
Percentage = 80.00
Division = First
'''

# roll = int(input('Enter your Roll number: '))
# name = input('Enter your name: ')
# p = int(input('Enter Physics marks: '))
# c = int(input('Enter Chemistry marks: '))
# m = int(input('Enter Maths marks: '))

# print('Roll No: ',roll)
# print('Name: ',name)
# print('marks in Physics: ',p)
# print('marks in maths: ',m)
# print('marks in chemistry: ',c)
# print('Total marks: ',p+c+m)
# per = (p+c+m)/300 *100
# print('Percentage: ',round(per,2))
# if per>=90:
#     print('Merit List')
# elif per>=75 and per<90:
#     print('Distinction')
# elif per>=60 and per<75:
#     print('First Class')
# elif per>=40 and per<60:
#     print('Second Class')
# else:
#     print('You are repeating the year')


'''
13. Write a C program to read temperature in centigrade and display a suitable message according to the temperature state below:
Temp < 0 then Freezing weather
Temp 0-10 then Very Cold weather
Temp 10-20 then Cold weather
Temp 20-30 then Normal in Temp
Temp 30-40 then Its Hot
Temp >=40 then Its Very Hot
Test Data :
42
Expected Output :
Its very hot.
'''
# temp = int(input('Enter the temperature in centigrade: '))
# if temp<0:
#     print('Freezing weather!!')
# elif 0<=temp<=10:
#     print('Very cold weather')
# elif 10<=temp<=20:
#     print('Cold weather')
# elif 20<=temp<=30:
#     print('normal temperature')
# elif 30<=temp<=40:
#     print('its hot')
# else:
#     print('Its very hot')


'''
14. Write a C program to check whether a triangle is Equilateral, Isosceles or Scalene.
Test Data :
50 50 60
Expected Output :
This is an isosceles triangle.
'''
# a = int(input('enter side1: '))
# b = int(input('enter side2: '))
# c = int(input('enter side3: '))
# if a==b==c:
#     print('It is an equilateral triangle')
# elif a == b or a == c or b==c:
#     print('It is an Isosceles Triangle')
# else:
#     print('Its an Scalene Triangle')


'''
15. Write a C program to check whether a triangle can be formed with the given values for the angles.
Test Data :
40 55 65
Expected Output :
The triangle is not valid.
'''
# a = int(input('enter side1: '))
# b = int(input('enter side2: '))
# c = int(input('enter side3: '))
# if a+b+c==180:
#     print('It is a Valid Triangle')
# else:
#     print('It is not a Valid Temple')


'''
16. Write a C program to check whether a character is an alphabet, digit or special character.
Test Data :
@
Expected Output :
This is a special character.
'''
# c = input('Enter a character: ')
# if 'A'<=c<='Z' or 'a'<=c<='z':
#     print('The character is an Alphabet')
# elif c in '1234567890':
#     print('The character is a Digit')
# else:
#     print('The character is special')


'''
17. Write a C program to check whether an alphabet is a vowel or a consonant.
Test Data :
k
Expected Output :
The alphabet is a consonant.
'''
# c = input('Enter a character')
# if c in 'aeiouAEIOU':
#     print('The character is a vowel')
# else:
#     print('The character is consonant')

'''
18. Write a C program to calculate profit and loss on a transaction.
Test Data :
500 700
Expected Output :
You can booked your profit amount : 200
'''
#we need cost price and the selling price of cprice>sprice then profit or loss otherwise
# cp = int(input('Enter the cost price: '))
# sp = int(input('Enter the selling price: '))
# if cp<=sp:
#     print('You got a profit of ',sp-cp)
# else:
#     print('You get the loss of amout: ',cp-sp)

'''
19. Write a program in C to calculate and print the electricity bill of a given customer. The customer ID, name, and unit consumed by the user should be captured from the keyboard to display the total amount to be paid to the customer.

The charge are as follow :
Unit	Charge/unit
upto 199	@1.20
200 and above but less than 400	@1.50
400 and above but less than 600	@1.80
600 and above	@2.00
If bill exceeds Rs. 400 then a surcharge of 15% will be charged and the minimum bill should be of Rs. 100/
Test Data :
1001
James
800
Expected Output :
Customer IDNO :1001
Customer Name :James
unit Consumed :800
Amount Charges @Rs. 2.00 per unit : 1600.00
Surchage Amount : 240.00
Net Amount Paid By the Customer : 1840.00
'''

