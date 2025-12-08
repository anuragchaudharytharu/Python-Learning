# Create a class with methods to perform basic arithmetic operations and call them.

class Operations:
    
    def add(self, num1, num2):
        addition = num1+num2
        print(f"Addition is {addition}")
        
    def subtract(self, num1, num2):
        subtraction = num1-num2
        print(f"Subtraction is {subtraction}")
        
    def multiply(self, num1, num2):
        multiplication = num1*num2
        print(f"Multiplication is {multiplication}")
        
    def divide(self, num1, num2):
        division = num1/num2
        print(f"Division is {division}")

Calc = Operations()
Calc.add(10,5)
Calc.subtract(10,5)
Calc.multiply(10,5)
Calc.divide(10,5)