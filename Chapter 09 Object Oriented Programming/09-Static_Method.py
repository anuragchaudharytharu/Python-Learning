'''
    STATIC Methods
    
    Methods that don't use the self parameter (work at class level)
    It works at class level
    It's a decorator method that is used when we have a function/method inside the class that doesn't need self reference parameter
    For function without self parameter to work, we neeed to bring that function to class level
    @staticmethod is used for this

                class Student:
                        @staticmethod  #This is a Decorator
                        def college():
                            print("ABC College")

    Decorator ===>
        Decorator allow us to wrap another function inorder to extend the behaviour of the wrapped function, without permanently modifying it
        It's a function that takes a function, change their behaviour and then output that function


        NOTE : static method can't access or modify class state & generally used for utility
'''

class Student:
    college_name = "ABC College" 

    def __init__(self, fullName, marksObtained):
        self.name = fullName
        self.marks = marksObtained
        print("Adding new student in database")

    def getMarks(self):
        return f"{self.name} marks is {self.marks} of {self.college_name}"

    @staticmethod
    def greetings():
        print("Hello Student")



s1 = Student("Klien", 97)
s1.greetings() # Hello Student
print(s1.getMarks()) # Klien marks is 97 of ABC College