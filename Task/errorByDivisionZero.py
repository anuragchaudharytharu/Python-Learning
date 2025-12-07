# Write a program that takes two numbers and handles the error if division by zero occurs.
import numpy as np

num1 = float(input("Enter Your 1st Number: "))
num2 = float(input("Enter Your 2nd Number: "))
try:
    result = num1/num2
    if np.isnan(result) == False:
        print(f"It is divisible. Result output is {result}")        
except Exception as e:
    print(f"Error: {e}")
    
'''
    or we can also use this expection

    except ZeroDivsionError:
        print("Error: Cannot be divided by Zero")
'''