'''
    FOR Loop

    For loop are used for sequential traversal. Its used to traverse datatype like list, tuples, string etc

    for loops ======>
            for element in variableName:
                #some work
            
    for loop with else =====>                
            for element in variableName
                #some work
            else: 
                #work when loop ends
'''

nums = [1, 2, 3, 4, 5]
for val in nums:
    print(val) # prints all the elements in the list


vegetables = ["potato", "brinjal", "ladyfinger", "cucumber"]
for val in vegetables:
    print(val) # prints all the vegetables element inside the list

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for num in tup:
    print(num) # prints all the elements in the list

str = "HarvardCollege"
for char in str:
    print(char) # prints all the characters of the string

name = "CristianoRonaldo"
for char in name:
    if(char == "z"):
        print("z found")
        break
else: 
    print("END")