'''
    METHODS
    
    Methods are functions that belong to objects
    When we write functions inside class, then that functions is known as methods

            # creating class =====>
                    class Student:
                        def __init__(self, fullName):
                                self.name = fullName

                        # This a class method. self reference parameter is a must
                        def hello(self): 
                            print("hello", self.name)
            
            # creating object =====>
                    s1 = Student("Klien")
                    s1.hello() # calling/executing class method
'''

class Student:
    college_name = "ABC College" 

    def __init__(self, fullName, marksObtained):
        self.name = fullName
        self.marks = marksObtained
        print("Adding new student in database")

    def welcome(self):
        print("Welcome student,", self.name)
    
    def getMarks(self):
        return f"Your marks is {self.marks}"


s1 = Student("Klien", 97)
print(s1.name, s1.marks, s1.college_name) # Klien 97 ABC College
s1.welcome() # Welcome student, Klien
print(s1.getMarks()) # Your marks is 97