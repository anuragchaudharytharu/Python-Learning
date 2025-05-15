# CONDITIONAL STATEMENTS

# if-elif-else (SYNTAX)
'''
  if(condtion):
      statement1
  elif(condtion):
      statement2
  else:
      stalementN   
'''

age = 18
if (age >= 18):
    print("Can vote")
    print("Can drive")
else:
    print("Cannot vote & cannot drive")


light = "green"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")


num = 3
if(num > 2):
    print("greater than 2")
elif(num > 3):
    print("greater than 3")


marks = int(input("Enter your marks:"))
if (marks >=90):
    grade = "A"
elif(90 > marks and marks >=80):
    grade = "B"
elif(80 > marks >=70):
    grade = "C"
else:
    grade = "D"
print(f"Grade of the student -> {grade}")