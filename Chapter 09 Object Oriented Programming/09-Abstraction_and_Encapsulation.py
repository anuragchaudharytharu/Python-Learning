'''
    ABSTRACTION & ENCAPSULATION

    ABSTRACTION
        Hiding the implementation details of a class and only showing the essential features to the user

    
    ENCAPSULATION
        Wrapping data and functions into a single unit (object)
        All the previous code of class, constructor, object, methods that we have written, we have done encapsulation to them i.e we have wrapped them into a single unit (object)
'''

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        # This are the implementation details that we are hiding
        self.clutch = True
        self.acc = True
        # This is the essentail features that is shown to the user
        print("car started...")
        # This is called Abstraction.

car1 = Car() # We are wrapping the data and function into this object. This is called ENCAPSULATION
car1.start()