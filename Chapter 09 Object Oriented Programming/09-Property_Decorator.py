'''
    Property Decorator
        We use @property decorator or any method in the class to use the method as a property

        Whenever our attrivute value changes, it calls its function automatically and [rovide the new updated value

                @property
                def attributeNameThatChangesEveryTime(self):
                        .....
'''

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    '''
    # Traditional way 
    def calculatePercentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
    '''

    # using proprty method
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


stu1 = Student(98, 97, 99)
print(stu1.percentage) # 98.0%

stu1.phy = 86
print(stu1.phy) # 86
print(stu1.percentage) # 94.0%