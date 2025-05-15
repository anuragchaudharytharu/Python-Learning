"""
    CONSTRUCTOR ====> __init__ Function

    All classes have a function called __init__(), which is always executed/invoked when the class is being initiated i.e object is being created 

                # creating class =====>
                            class Student:
                                def __init__(self, fullName):
                                        self.name = fullName
                
                # creating object =====>
                            s1 = Student("Klien")
                            print(s1.name)
  
    NOTE: self parameter is a reference to the current instance of the object, and is used to access variables that belongs to the class. self parameter can be named anything like abcd etc
"""


class Student:

    # default constructors
    def __init__(self):
        pass

    # parameterized constructors
    def __init__(self, fullName, marksObtained):
        self.name = fullName
        self.marks = marksObtained
        print(self) # <__main__.Student object at 0x000001D113236F90>
        print("Adding new student in database") # Adding new student in database

s1 = Student("Klien", 97) # This is the current intances of the object. "Klien" is the name parameter value
print(s1) # <__main__.Student object at 0x000001D113236F90>
print(s1.name, s1.marks) # Klien 97
 
s2 = Student("Peter", 88) # "Peter" is the name parameter value
print(s2) # <__main__.Student object at 0x0000015E46228B90>
print(s2.name, s2.marks) # Peter 88