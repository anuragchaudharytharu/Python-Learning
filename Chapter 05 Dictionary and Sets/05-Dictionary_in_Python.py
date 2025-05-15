'''
    DICTIONARY

    Dictionaries are used to store data values in "key":value pairs

    They are unordered, mutable(changeable)
    Doesn't allow duplicate keys

    All datatypes can be used as value
    Only immutable datatypes can be used as key such as strings, tuples, float, integer, boolean
    We cannot use dictionary as a key as it is unhashable

            variableName = {
                key : value
            }


    To overwrite value or assign/add new key:value pair
            variableName["key"] = value
    
    To get all keys
            variableName.keys()
'''

dict = {
    "name" : "John Doe",
    "cgpa" : 9.6,
    "marks" : [98, 97, 95],
    12 : True,
    True: "Pass",
    40.444 : "float",
    ("mango", "banana") : "fruits",
    "favourite" : {
        "fruit" : "mango",
        "vegetables" : "brijal",
        "sweets" : "chocolate",
        "movie" : "The Godfather"
    }
}

print(type(dict)) # <class 'dict'>

print(dict["name"]) # John Doe
print(dict["cgpa"]) # 9.6
print(dict["marks"]) # [98, 97, 95]

print(dict[("mango", "banana")]) # fruits
print(dict[True]) # Pass
print(dict[40.444]) # float
print(dict[12]) # True


print(type(dict["favourite"])) # <class 'dict'>
print(dict["favourite"]) # {'fruit': 'mango', 'vegetables': 'brijal', 'sweets': 'chocolate', 'movie': 'The Godfather'}
print(dict["favourite"]["movie"]) # The Godfather

dict["age"] = 24
print(dict) # {'name': 'John Doe', 'cgpa': 9.6, 'marks': [98, 97, 95], 12: True, True: 'Pass', 40.444: 'float', ('mango', 'banana'): 'fruits', 'favourite': {'fruit': 'mango', 'vegetables': 'brijal', 'sweets': 'chocolate', 'movie': 'The Godfather'}, 'age': 24}

dict["name"] = "Alan Murphy"
print(dict) # {'name': 'Alan Murphy', 'cgpa': 9.6, 'marks': [98, 97, 95], 12: True, True: 'Pass', 40.444: 'float', ('mango', 'banana'): 'fruits', 'favourite': {'fruit': 'mango', 'vegetables': 'brijal', 'sweets': 'chocolate', 'movie': 'The Godfather'}, 'age': 24}


# Conversion =====> Type casting dictionary
favourite = {
    "fruit" : "mango",
    "vegetables" : "brijal",
    "sweets" : "chocolate",
    "movie" : "The Godfather"
}
print(list(favourite)) # ['fruit', 'vegetables', 'sweets', 'movie']
print(type(str(favourite))) # <class 'str'>
print(tuple(favourite)) # ('fruit', 'vegetables', 'sweets', 'movie')