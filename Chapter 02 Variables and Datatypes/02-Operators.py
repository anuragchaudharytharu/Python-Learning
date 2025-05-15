# OPERATORS
# An operators is a symbol that performs a certain operation between operands

# AIRTHMETIC OPERATOR ( +, -, *, /, %, ** )
a = 5
b = 2

print(a + b) # 7 =====> Addition.
print(a - b) # 3 =====> Subtraction.
print(a * b) # 10 =====> Multiplication.
print(a / b) # 2.5 =====> Division. It always give floating datatype value
print(a % b) # 1 =====> It shows remainder as an output result
print(a**b) # 25 =====> It's a power operation like in here the result is 25 which is from 5 ^ 2 = 25



# RELATIONAL OPERATORS ( ==, !=, >, <, >=, <= )
# It gives boolean value as an output
a = 50
b = 20

print(a == b) # False =====> Checks if a is equal to b
print(a != b) # True =====> Checks if a is not equal to b
print(a > b) # True =====> Checks if a is greater than b
print(a < b) # False =====> Checks if a is lesser than b
print(a >= b) # True =====> Checks if a is greater than and equal to b, If any of the condition i.e greater than/equalto staisfy to be True then the output result will be True 
print(a <= b) # False =====> Checks if a is lesser than and equal to b, If any of the condition i.e lesser than/equalto staisfy to be True then the output result will be True 



# ASSIGNMENT OPERATOR ( =, +=, -=, *=, /=, %=, **= )
a = 10
a += 2 # a = a + 2
print(a) # 12 =====> 10+2 = 12

b = 10
b -= 2
print(b) # 8 =====> 10-2 = 8

c = 10
c *= 2
print(c) # 20 =====> 10*2 = 20

d = 10
d /= 2
print(d) # 5 =====> 10/2 = 5.0 This output is always a floating datatype

e = 10
e %= 2
print(e) # 0 =====> 10%2 = 0 is the remainder we get when we do 10/2

f = 10
f **= 2
print(f) # 100 =====> 10**2 = 100


# LOGICAL OPERATOR ( not, and, or )
a = 50
b = 30
val1 = True
val2 = True

print(not False) # True
print(not True) # False
print( 'not OPERATOR (i.e gives result of opposite booloean value):', not(a > b)) # False

print('and OPERATOR (i.e for the result to be True, both condition should be True):', val1 and val2) # True
print('and OPERATOR (i.e for the result to be True, both condition should be True):', (a == b)  and (a >= b)) # False

print('or OPERATOR (i.e for the result to be True, any1 of the condition should be True):', (a == b)  and (a >= b))