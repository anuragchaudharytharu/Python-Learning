'''
    INHERITANCE
        When one class(child/derived) derives the properties & methods of another class(parent/base)

                        class Car:
                            ......
                        
                        class ToyotaCar(Car):
                
                            ......
    
        There are 3 types of Inheritance:
            Single Inheritance ====>
                    When a single child class inherit parent class properties and methods, it's called single inheritance
                                parent ====> child 
            Multi-Level Inheritance
                    When inheritance of parent class properties and methods goes from one child class to another child class and so on to the multiple generational level, it's called multi-level inheritance
                                parent ====> child ====> child and so on
            Multiple Inheritance
                    When child class inherit propeties and methods from multiple parent class, it's called multiple inheritance
                                parent1 ====> child <==== parent2
                            There is only one child but many parent 

'''

# SINGLE INHERITANCE
class Bike:
    color = "Black Bike"

    @staticmethod
    def start():
        print("Bike Started....")
    
    def stop(self):
        print("Bike Stopped....")

class Yamaha_Bike(Bike):
    def __init__(self, name):
        self.name = name

bike1 = Yamaha_Bike("Yamaha")

print(bike1.name)
print(bike1.start())
print(bike1.stop())
print(bike1.color)




# MULTI_LEVEL INHERITANCE
class Car:
    color = "Red Car"

    @staticmethod
    def start():
        print("Car Started....")

    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Factory(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Factory("EV")
car1.start()
print(car1.type)




# MULTIPLE INHERITANCE
class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)