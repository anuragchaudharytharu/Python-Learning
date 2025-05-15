'''
    Class & Instance Attributes

    Attributes are the data that we provide.
    There are two types of attributes in classes and they are:
            Class.attr
            Obj.attr

    Class.attr ====> 
                Class Attribute
                Generally class.attr are those attributes that have same value throughout different objects/instances created
    Obj.attr ====> 
                Object/Instance Attribute
                Generally obj.attr are those attributes that has different value for different objects/instances created
                self reference to the object created must be provided

    
    NOTE ====> 
        Obj.attr priority is greater than Class.attr in uses

        It is also possible to change attribute value directly
'''

class Student:
    college_name = "ABC College" 
    name = "anonymous" # This is a class attribute

    def __init__(self, fullName, marksObtained):
        self.name = fullName # This is a object attribute
        self.marks = marksObtained # This is a object attribute
        print("Adding new student in database")

s1 = Student("Klien", 97)
print(s1.name, s1.marks, s1.college_name) # Klien 97 ABC College
print(Student.name) # anonymous

# changing attribute value
s1.name = "Mouse"
print(s1.name) # Mouse
 
s2 = Student("Peter", 88)
print(s2.name, s2.marks, Student.college_name) # Peter 88 ABC College
print(Student.name) # anonymous