#  Write a program that handles the error when trying to open a file that does not exist.

def fileNotFound(fileName):
    try:
        with open(fileName, "r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError as e:
        print(e)
        
fileNotFound(r"D:\Artificial Intelligence Engineer\Python\Python Learning\Task\sampl.txt")        