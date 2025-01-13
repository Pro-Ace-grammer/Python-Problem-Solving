'''
Python program that takes two user input numbers and performs their division,
Handle the following exceptions

ZeroDivisionError: If the second number is zero
ValuError: if the user enters a non-numeric values

'''

try:
    a = int(input('a: '))
    b = int(input('b: '))
    div=a/b
    print(f"Division = {div}")
except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter a numeric value")

