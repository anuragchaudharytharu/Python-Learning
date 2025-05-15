'''
    FUNCTIONS in Python

    Block of statements that perform a specific task
    First we need to define the function and then at last we need to call the function by providing argument value to the parameter
    

            def functionName(parameter1, parameter2,..):
                    #some work, value
                    return value

            functionName(arugument1, arguement2,..)

        NOTE: only 1st paramete and its argument are default as non-default arguments i.e 2nd, 3rd,... paramter & argument follows 1st parameter & argument
            
    Return Statement ======>
            Functions send Python values/objects back to the caller.
            These values/objects are known as the function's return value
'''

def difference(x, y):
    diff = x - y
    print(diff)
difference(12, 6)


def printHello():
    s = "Hello"
output = printHello()
print(output) # None =====>  because we are not returning variable s


def multiply(num1, num2):
    result = num1 * num2
    return result
print(multiply(6, 8)) # 48


def multiply(num1, num2):
    result = num1 * num2
    return result
x = multiply(6, 8)
print(x) # 48


def division(a, b):
    return a / b
c = division(100, 25)
print(c) # 4.0 ====> division operator always return float datatype as an output