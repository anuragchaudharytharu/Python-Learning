'''
    Define a Employee class with attributes role, department & salary. This class has also a showDetails() method
    Create an Engineer class theat inherits properties from Employee & has additional attributes : name & age
'''

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(f"role = {self.role}")
        print(f"department = {self.department}")
        print(f"salary = {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "$75000")

e1 = Employee("Accountant", "Finance", "$60000")
e1.showDetails()

engg1 = Engineer("Klien Morriarty", "25")
engg1.showDetails()