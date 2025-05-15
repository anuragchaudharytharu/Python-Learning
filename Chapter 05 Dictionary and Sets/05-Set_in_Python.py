'''
    SET in Python
    
    Set is the collection of the unordered items

    Each element in the set must be unique & immutable
    Set are mutable but its element are not mutable

    Doesnot accept mutable type like list, dictionary

    num = {1,2,3,4,5}

    set2 = {1,3,2,2,4,2} =======> repeated are elements stored only once, so its resolved to set2 = {1, 2, 3, 4}

    null_set = set() =======> empty set syntax
'''

collection = {1,3,2,2,4,2, "hello","world","world", True, None, (2, 3, 2)}
print(type(collection)) # <class 'set'>
print(collection) # {None, 1, 2, 3, 4, 'hello', (2, 3, 2), 'world'}

print(len(collection)) # 8 =======> total count/length of items inside set

# to write empty set
Set1 = set() # ======> empty set syntax
print(type(Set1)) # <class 'set'>
print(Set1) # set()