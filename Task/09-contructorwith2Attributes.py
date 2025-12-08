# Create a class with a constructor that initializes two attributes and displays them.

class Student:
    def __init__(self, fullName, Age):
        self.fullname = fullName
        self.age = Age

s1 = Student("Klien Morriarty", 97)
print(f"{s1.fullname} is of age {s1.age}")