class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print(self.role)
        print(self.dept)
        print(self.salary)
    
class Engineer(Employee):
    def __init__(self, name, age, role, dept, salary):
        super().__init__(role, dept, salary)
        self.name = name
        self.age = age
    
    def showDetails(self):
        print(self.name)
        print(self.age)
        super().showDetails()

engg = Engineer('Arsu',22,'SD','IT',95000)
engg.showDetails()