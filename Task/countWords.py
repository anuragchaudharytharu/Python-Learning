# Write a program to count the number of words in a given text file.

with open(r"D:\Artificial Intelligence Engineer\Python\Python Learning\Task\sample.txt", "r+") as file:
    data = file.read()
    print(data)
    
    words = data.split()
    print(words)
    
    number_of_words = len(words)
    print(number_of_words)