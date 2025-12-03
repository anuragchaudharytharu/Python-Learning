'''
    Note :Set is mutable but its elements are immutable. That's why we cannot pass list, dictionary as an element because they are mutable and are unhashable type

    Hash value ====> Every data has a specific hash value. Immutable data are hasable because their hash value doesn't change. Mutable data are unhasable because their hash value changes everytime the data is changed/transformed. 
'''

collection = set() # empty set

# .add(element) ======> adds specified element. It only accept one argument
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3)
collection.add("mouse")
print(collection) # {1, 2, 3, "mouse"}


# .remove(element) ======> removes specified element. If the element to be removed is not present inside set, then it gives error
collection.remove(3)
print(collection) # {1, 2, "mouse"}


# .pop() =======> removes a random value
collection.pop()
print(collection)


# .clear() ======> empties the set
collection.clear()
print(len(collection)) # 0
print(collection) # set()




# SET UNION and INTERSECTION
set1 = {1,2,3, "rat", 2}
set2 = {"rat", 3, 4, 5, 3}

# .union(set2) ======> combines both set values & returns a new set
union_set = set1.union(set2)
print(union_set) # {1, 2, 3, 'rat', 4, 5}


# .intersection() =======> combines common values and returns a new set
intersection_set = set1.intersection(set2)
print(intersection_set) # {3, 'rat'}