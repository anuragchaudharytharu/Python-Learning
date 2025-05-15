'''
    LISTS in Python

    A built in datatype that stores set of values
    It can store elements of different types (integer, float, strings, etc)

    LISTS are mutable
'''

a = [] # This is an empty Lists
print(a) # []




b = ["max"]
print(type(b)) 
print(b)




info = [94.4, True, "John Doe", 66, 45.1]

print(info) # [94.4, True, "John Doe", 66, 45.1]
print(len(info)) # 5
print(type(info)) # <class 'list'>
print(info[0]) # 94.4
print(info[2]) # John Doe

info[len(info)-1] = "Last Index"
print(info) # [94.4, True, 'John Doe', 66, 'Last Index']