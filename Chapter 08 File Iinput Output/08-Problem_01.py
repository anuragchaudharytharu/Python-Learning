''' 
    Create a new file "practice.txt" using python. Add the following data in it
            Hi everyone
            we are learning File I/O
            using Java
            I like programming in Java
'''

data = '''Hi everyone
we are learning File I/O
using Java
I like programming in Java'''

with open("practice.txt", "w") as f:
    addData = f.write(data)