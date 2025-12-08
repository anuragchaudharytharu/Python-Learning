# Write a program to read a text file and print each line with line numbers.

# 1st Method
with open(r"D:\Artificial Intelligence Engineer\Python\Python Learning\Task\sample.txt", "r") as file:
    lines = file.readlines()
    print(type(lines))
    totalLineNumber = len(lines)
    print(totalLineNumber)
    
    for eachLineData in lines:
        lineNumber = lines.index(eachLineData) + 1
        print(lines.index(eachLineData) + 1, eachLineData)
 
    
# 2nd Method
def lineNumber(fileName):
    with open(fileName) as file:
        for lineIndex, lineData in enumerate(file):
            pass
    totalLineNumber = lineIndex + 1
    return totalLineNumber
print(lineNumber("D:\Artificial Intelligence Engineer\Python\Python Learning\Task\sample.txt"))

# 3rd Method
try: 
    with open("D:\Artificial Intelligence Engineer\Python\Python Learning\Task\sample.txt", mode="r") as file:
        for i, j in enumerate(file):
            num= i+1
            pass
    print(num)
except FileNotFoundError:
    print("Error: Specified File Not Found")

# 4th Method
try:
    with open("D:\Artificial Intelligence Engineer\Python\Python Learning\Task\sample.txt", "r") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"{line_number}: {line.rstrip()}")
        print(line_number)
except FileNotFoundError:
        print("Error: The specified file was not found.")        