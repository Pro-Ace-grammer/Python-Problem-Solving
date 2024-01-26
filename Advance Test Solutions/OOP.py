'''
Consider a company that has employees and managers. The Person class represents
basic information about an individual, the Employee class extends person to include
employee-specific details such as an employee ID, and the Manager class further extends
Employee to include the department they manage
'''


class Person:
    name = input('name: ')
    age = input('Enter Age')
    
    def __str__(self):
        return self.name


class Employee(Person):
    eid = input('Eid: ')
    def __init__(self):
        super()

    def display_info(self):
        print(self.eid)
        print(self.name)
        print(self.age)
        print('\n\n')
        

class Manager(Employee):
    def __init__(self):
        super()
        self.dept = input('department: ')

    def display_info(self):
        print()
        print(self.eid)
        print(self.name)
        print(self.age)
        print(self.dept)
        
        
a = Employee()
a.display_info()

b = Manager()
b.display_info()
