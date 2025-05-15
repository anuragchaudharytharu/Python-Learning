# (WAF) Write a function that replace all ocurances of "java" with "python" in the above line

def replace_function():
    with open("practice.txt", "r") as f:
        data = f.read()
        
        newData = data.replace("Java", "Python")

        with open("practice.txt", "w") as f:
            f.write(newData)

replace_function()