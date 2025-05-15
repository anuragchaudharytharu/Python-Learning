# There are two type of conversions and they are
# 1. Type Conversion ======> python interpretor automatically do type conversion
# 2. Type Casting =======> we have to convert the type mannually


#Type Conversion ==> automatic conversion
a = 2
print(type(a)) # <class 'int'>
b = 4.25
sum = a + b # 2.0 + 4.25 = 6.25
#here python convert type of variable a into superior datatype i.e from integer to float number before addition operation
print(type(sum)) # <class 'float'>




#Type casting
c = float('2') # mannual typer conversion of string to float datatype
print(type(c)) # <class 'float'>
d = 4.25
add = c + d
print(type(add)) # <class 'float'>

a = 3.14
a = str(a) # '3.14'
print(a)
print(type(a)) #<class 'str'>

favourite = {
    "fruit" : "mango",
    "vegetables" : "brijal",
    "sweets" : "chocolate",
    "movie" : "The Godfather"
}
print(list(favourite)) # ['fruit', 'vegetables', 'sweets', 'movie']
print(tuple(favourite)) # ('fruit', 'vegetables', 'sweets', 'movie')