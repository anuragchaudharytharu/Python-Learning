'''
    Private (like) attributes & methods

        Conceptual Implementation in Python
        They are like a imitation of private attributes or methods but not an actual private attributes or methods

            Private attributes & methods are meant to be used only within the class and are not accessible from outside the class

                                self._name = attributeValue
        
            Double Underscore infront of attributeName or functionName like (_name) is used to specify that this is a private attribute or private methods

            NOTE: private attributes & methods can only be accessed by internal function of class

    All of the functions/attributes we used in class before are public
'''

class Account:
    def __init__(self, acc_no, acc_pass):
        self.__acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")
print(acc1.reset_pass()) #None
print(acc1.__acc_no) #throws error



class Person():
    __name = "anonymous"

    def __hello(self):
        print("Hello User")
    
    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome)