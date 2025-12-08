# Write a program that asks the user for an integer and handles invalid input.

import numpy as np

try:
    num = int(input("Enter Integer: "))
    if np.isnan(num) == False:
        print(f"User input integer {num} is Valid")
except Exception as e:
    print(f"Error: {e}. Please Input an integer")
    