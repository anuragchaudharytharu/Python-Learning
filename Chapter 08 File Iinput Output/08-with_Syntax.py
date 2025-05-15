'''
    with Syntax

    Its a better way to write file i/o in python

                with open("file_name", "mode") as f:
                            #some work

    NOTE: as ====> aliases
          closing the file is not compulsory when using with Syntax
'''

with open("demo.txt", "rt") as file:
    data = file.read()
    print(data)

with open("sample.txt", "a") as addingNewLine:
    newLine = addingNewLine.write("\nThis is a new line.")
    