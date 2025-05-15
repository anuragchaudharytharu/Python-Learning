'''
    POLYMORPHISM : Operator Overloading

    When the same operator is allowed to have different meaning according to the context

        Opertor & Dunder functions

            a + b   #addition          <=====>       a.__add__(b)
            a - b   #subtraction       <=====>       a.__sub__(b)
            a * b   #multiplication    <=====>       a.__mul___(b)
            a / b   #division          <=====>       a.__truediv___(b)
            a % b   #modulo            <=====>       a.__mod___(b)

    Dunder Functions ====> Whenever we perform an operation, let's say (A + B), then internally in that specific class, we call dunder function for A in which we pass B
'''

print(1 + 2) # 3
print("apna" + "college") # apnacollege =====> concatenation
print([1, 2, 3] + [4, 5, 6]) # [1, 2, 3, 4, 5, 6] =====> merge


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def showNumber(self):
        print(f"{self.real}i + {self.imaginary}j")

    # Dunder Function
    # a.__add__(b)
    def __add__(self, obj2):
        newReal = self.real + obj2.real
        newImaginary = self.imaginary + obj2.imaginary
        return Complex(newReal, newImaginary)
    
    # a.__sub__(b)
    def __sub__(self, obj2):
        newReal = self.real - obj2.real
        newImaginary = self.imaginary - obj2.imaginary
        return Complex(newReal, newImaginary)
    

num1 = Complex(1, 3) # 1st object
num1.showNumber()

num2 = Complex(4, 6) # 2nd object
num2.showNumber()

'''
num3 = num1.add(num2) #this is a method way to call addition function. Same operation can be done by using dunder function when we create function for the method
'''
num3 = num1 + num2
num3.showNumber()

num3 = num1 - num2
num3.showNumber()

'''
    num1.add(num2) call class function named addition(self, obj2), passing num2 as parameter value for obj2. num2 = Complex(4, 6) where 4 is self.real = real and 6 is self.imaginary = imahinary  from the constructor function. So, as num2 is passed as value of obj2 parameter, 4 is given to obj2.real and 6 is given to obj2.imaginary.

    num1.add(num2) when calls addtion(self, obj2) function, it means For num1, self.real and self.imaginary are from original constructor function in which we pas 1, 3 as the value of real and imaginary parameter

    And then we add obj2 and self real together creating newReal. same with obj2 and self imaginary creating newImaginary

    And at last we return Complex(newReal, newImaginary) to make the value available globally


    In simple terms: 
        In addition(self, obj2):
                obj2.real = num2.real = 4
                obj2.imaginary = num2.imaginary = 6

                self.real = num1.real = 1
                self.imaginary = num1.imaginary = 3

                newReal = self.real + obj2.real
                newImaginary = self.imaginary + obj2.imaginary

                Complex(newReal, newImaginary)
'''