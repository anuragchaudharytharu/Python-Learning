'''
try...except
            try..except blocks are used in python to handle wrrors and exceotions.
            The code in (try) block runs when there is no error.
            If (try) block catches the error, then the except block is executed

                            try:
                                ...block of code that tests for error
                            except:
                                ...block of code that handle errors
                            else: 
                                ...block of code that executes when there is no error
'''

a = input("Enter the number:")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except Exception as e:
    print("Error:", e)
    print("Invalid Input")

print("Some Line of codes")
print("End of program")




try:
    num = int(input("Enter an Integer:"))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")
else:
    print("End of the program")