'''
    class Method

    A class method is bound to the class & recieves the class as an implicit first argument

    NOTE: Static Method can't access or modify class state & generally used for utility

                class Student:
                    @classmethod  #decorator
                    def college(cls):
                        pass
'''

class Person:
    name = "anonymous"
    age = 30
    occupation = "AI Engineer"
    description = "He is an exellent ai engineer"

    def changeNameNotChanged(self, name):
        self.name = name
    
    def changeAge(self, age):
        Person.age = age # 1st way to change class attributes

    def changeOccupation(self, occuapation):
        self.__class__.occupation = occuapation # 2nd way to change class attributes

    # @classmethod =====> It's a decorator. It's a 3rd way to change class attribute value directly inside functions
    @classmethod
    def changeDescription(cls, description): # cls ===> we take class as parameter here
        cls.description = description


p1 = Person()

p1.changeNameNotChanged("Anurag Chaudhary Tharu")
print(p1.name) # Anurag Chaudhary Tahru
print(Person.name) # anonymous

p1.changeAge(18)
print(p1.age) # 18
print(Person.age) # 18

p1.changeOccupation("AI Researcher")
print(p1.occupation) # AI Researcher
print(Person.occupation) # AI Researcher

# @classmethod