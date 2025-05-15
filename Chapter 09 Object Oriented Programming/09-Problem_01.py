# Create student class that takes name & marks of 3 subjects as arguements in constructor. Then create a method to print the average

class Student:
    # constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    # method
    def get_average(self):
        sum = 0
        for value in self.marks:
            sum += value
        print(f"Hi {self.name}, your average score is {sum/3}")

s1 = Student("Peter Quil", [88, 90, 94])
s1.get_average() # Hi Peter Quil, your average score is 90.66666666666667

s1.name = "Klien Morriarty"
s1.get_average() # output: Hi Klien Morriarty, your average score is 90.66666666666667
