'''
    BUILT-IN Functions

    print() =====> to print our value
            print(values)

    len() ======> find the length of the value
            .len(vaiableName)
    type() ======> fint type of the data, value, variableName
            .type(variableName)
    range() ======>  to find value of a limited range
        range(start?, stop, step?)
'''

'''
    USER-DEFINED functions
    
    all the functions that we write for certain tasks are the user defined functions
'''

print('apnacollege', "harvardcollege") #sep = " " =======> there is built-in separator function when we use comma and it prints in same line


# Both pritns in different line
print('apnacollege') 
print("harvardcollege")


# Both prints in same line as there is end = " " function given inside first print function 
print('apnacollege', end = " ") 
print("harvardcollege")


# .len() =====>  find the length of the value
nums = [1, 2, 3.4]
length_of_nums = len(nums)
print(length_of_nums) # 3


# range() =====> get the value within a limited range
for nums in range(0, 10, 2):
    print(nums)