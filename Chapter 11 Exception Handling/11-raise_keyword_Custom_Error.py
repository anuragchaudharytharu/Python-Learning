'''
    Custom Error: raise Keyword

    In Python, we can raise custom errors by using raise keyword
    Sometimes we may need to create our own exceptions that serve our purposes

    Defining Custom Exceptions
        In Python, we can define custom exceptions by creeating a new class that is derived from the bult-in Exception class
                Syntax:
                        class CustomError(Exception):
                            # code ....
                            passs
                        try:
                            # code ....
                        except CustomError:
                            # code ....

        This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending a report to the admin, calling an api, etc
'''

a = int(input("Enter any value between 5 and 9 :"))

if(a < 5 or a > 9):
    raise ValueError("Value should be between 5 and 9")
