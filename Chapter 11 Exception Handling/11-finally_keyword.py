'''
    FINALLY Clause

    When we handle exception using try and except block, we can include a finally block at the end.
    The finally block is always executed, so its generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message

                        try:
                            ...block of code that tests for error
                        except:
                            ...block of code that handle errors
                        else: 
                            ...block of code that executes when there is no error
                        finally:
                            ...block of code is always executed            
'''

def func1():    
    try:
        l = [1, 5, 6, 7]
        i = int(input("enter the index:"))
        num = l[i]
        return num
    except:
        return "Some error occured"
    finally:
        print("I am always executed")

x = func1()
print(x)