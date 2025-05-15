# Inputs In Python
# input() statement is used to accept values (using keyboard) from the user
# input() result is always a string datatype

name = input('enter your name: ')

print(type(name)) # <class 'str'>
print("Welcome", name)

age = input('enter your age: ')
print(type(age)) # <class 'str'>
print("Your age is", age)

favouriteNumber = float(input('enter your favourite number:'))
print(type(favouriteNumber)) # <class 'float'>
print("Your Favourite Number is", favouriteNumber)