str = "i am a coder."

# .endswith(word) =====> returns true if string ends with specifies substr
endswith = str.endswith("er.")
print(endswith) # True


#.capitalize() ======> capitalizes 1st character
str = str.capitalize()
print(str) # I am a coder.

#.repalce(old, new) =======> replaces all occurances of old with new
str = str.replace("coder", "programmer")
print(str) # I am a programmer.
newStr = str.replace('r', "e")
print(newStr) # I am a peogeammee.

# .find(word) ======> returns 1st index of 1st occurer
str1 = "I am studying Python from Harvard Python Course"
print(str1.find("Python")) # 14 ======> Python start from 5th index position in the string

# .count(word) ======> counts the occurances of substr
str2 = "I am studying Python from Harvard Python Course"
print(str2.count("Python")) # 2 =====> total occurance of the word "Python" is 2 inside the string
print(str2.count("r")) # 4 =====> total occurance of the character "r" is 4 inside the string