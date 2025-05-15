'''
    TUPLES
    A built-in data type that lets us create immutable sequence of values

    Its immutable i.e we cannot change/assign new value to it

    Note: When we have only one element inside the tuple, we have to provide comma after the element. If we don't do this then python doesnot consider that value to be of type tuple
'''

bird = ("parrot") # there is no comma after "parrot" which is why python consider bird variable to be string
print(type(bird)) # <class 'str'>
print(bird) # "parrot"




a = () # this is an empty tuple
print(a) # ()




num = (100,)
print(type(num)) # <class 'tuple'>




tup = (87, 64.55, "Cat", None, True)

print(len(tup)) # 5
print(type(tup)) # <class 'tuple'>
print(tup[0]) # 87
print(tup[3]) # None
print(tup[2]) # Cat
print(tup[len(tup) - 1]) # True
