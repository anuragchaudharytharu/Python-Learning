'''
    Super Method

        super() method is used to access methods of the parent class from child class
'''

class Car:
    color = "Red Car"

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started....")

    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start() # This start as soon as we create object like in here is car1

car1 = ToyotaCar("Prius", "Electric Vehicle")
print(car1.type)