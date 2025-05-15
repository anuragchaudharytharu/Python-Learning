"""
    CLASS & OBJECT in Python

    Class is a blueprint for creating objects
    Generally, when we name the class, we start with captical letter
    Class is made up of two things:
        1: Data (attributes)
        2: Methods

                creating class =====>
                            class Student: 
                                name = "Klien Morriarty"

                creating object (instance) =====>
                            s1 = Student()  #calling class
                            print(s1.name)

                            # changing value of attribute
                            s1.name = "Pter Quil"
                            print(s1.name)

    NOTE ====> 
        We cannot use class directly. To use it, we need to create object (instances)

        It is also possible to change attribute value directly

    
    There are Four Pillers of class and they are:
            ABSTRACTION
            ENCAPSULATION
            INHERITANCE
            POLYMORPHISM
"""

class Student:
    name = "Klien Morriarty"

s1 = Student()
print(s1) # <__main__.Student object at 0x000002D1CF366F90>
print(s1.name) # Klien Morriarty
print(Student.name) # # Klien Morriarty

# changing attribute value
s1.name = "Mouse"
print(s1.name)

s2 = Student()
print(s2.name) # Klien Morriarty
print(Student.name) # # Klien Morriarty



class Car:
    color = "blue"
    brand = "lamborghini"

car1 = Car()
print(car1.color) # blue
print(Car.color) # blue
print(car1.brand) # lamborghini
print(Car.brand) # lamborghini