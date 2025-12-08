# Write a program to create a file and write five lines of text into it.

turn = ["1st", "2nd", "3rd", "4th", "5th"]
data = ""
with open(r"D:\Artificial Intelligence Engineer\Python\Python Learning\Task\5lines.txt", "w+") as file:
    for i in range(5):
        data = input(f"Enter Your {turn[i]} data: ")
        file.write(f"{data} \n") 
           
    # Move the cursor to the beginning before reading
    file.seek(0)
    # Read File before streaming
    print(file.read())