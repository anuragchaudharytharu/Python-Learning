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


# .keys() ======> returns all keys
print(dict.keys()) # dict_keys(['name', 'cgpa', 'marks', 12, True, 40.444, ('mango', 'banana'), 'favourite'])




# .len(variableName.values()) ======> returns total count/length of keys
print(len(dict)) # 9 =====> length of key:value pairs
print(len(dict.keys())) # 9 ======> total count/length of keys




# .values() =======> returns all values 
print(dict.values()) # dict_values(['Alan Murphy', 9.6, [98, 97, 95], True, 'Pass', 'float', 'fruits', {'fruit': 'mango', 'vegetables': 'brijal', 'sweets': 'chocolate', 'movie': 'The Godfather'}, 24]) 




# .len(variableName.values()) =====> returns total count/length of values
print(len(dict)) # 9 =====> length of key:value pairs
print(len(dict.values())) # 9 ======> toal count/length of values




# .items() ======> returns all key:value pairs as tuples (key, value) pairs and its datatype becomes dict_items
items = dict.items()
print(items) # dict_items([('name', 'John Doe'), ('cgpa', 9.6), ('marks', [98, 97, 95]), (12, True), (True, 'Pass'), (40.444, 'float'), (('mango', 'banana'), 'fruits'), ('favourite', {'fruit': 'mango', 'vegetables': 'brijal', 'sweets': 'chocolate', 'movie': 'The Godfather'})])
print(type(items)) # <class 'dict_items'>

pairs = list(items)
print(pairs[0]) # ('name', 'John Doe')




# .get(key) ======> returns value of specified key. Note: It doesnot give error when there is no specified key inside the dictionay unlike when we use [key] to access its value which in that case crashes our application. It just returns None as an output and doesnot crash our application
print(dict.get("name")) # John Doe
print(dict.get("number")) # None =====> There is no "number" key inside the dictionary




# .update(newDictionary) =======> inserts the specified items to the dictionary
dict.update({"city" : "Melbourne", "Major": "Artificial Intelligence", "name": "Lin Mei"})
print(dict) # {'name': 'Lin Mei', 'cgpa': 9.6, 'marks': [98, 97, 95], 12: True, True: 'Pass', 40.444: 'float', ('mango', 'banana'): 'fruits', 'favourite': {'fruit': 'mango', 'vegetables': 'brijal', 'sweets': 'chocolate', 'movie': 'The Godfather'}, 'city': 'Melbourne', 'Major': 'Artificial Intelligence'}