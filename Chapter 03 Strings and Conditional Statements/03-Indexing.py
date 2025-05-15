# INDEXING ====> position

'''
  A N T I   C A M P U S
  0 1 2 3 4 5 6 7 8 9 10  =====> +ve indexing position

  A  P  P  L  E
  -5 -4 -3 -2 -1 =====> -ve indexing position
'''

''' 
  Index always start from 0th position
  It's only used to access characters from their specific index position
  We cannot modify/manipulate string charaters by using indexing
'''

str = "Anti Campus"
ch = str[0]
print(ch) # A =======> Oth index position character
print(str[5]) # C =======> 5th index position character

'''
str[3] = "m" #   We cannot modify/manipulate string charaters by using indexing
print(str) #throws error
'''