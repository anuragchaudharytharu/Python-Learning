# SLICING ======> Accessing parts of a string
'''
  str[startingIndex : endingIndex] ======> endIndex is not included

  when we don't specify both startingIndex and endingIndex, python automatically takes 0th for startingIndex and length of the string for endingIndex

  when we dont provide startingIndex but only provide endingIndex, python takes 0th index as the startingIndex

  when we only provide startingIndex but don't provide endingIndex, python automatically takes length of the string as endingIndex
'''

string = "HarvardCampus"
slicedString = string[0:5]
print(slicedString) # Harva

str1 = "Apna College"
print(str1[5:12]) # College
print(str1[5:len(str1)]) # College

str2 = "Dune Prophecy"
print(str2[5:]) # Prophecy # str2[5:len(str2)]
print(str2[:]) # Dune Prophecy #str2[0:len(str2)]
print(str2[:10]) # Dune Proph  #str2[0:10]

str = "Apple"
print(str[-3: -1]) # pl