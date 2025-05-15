# Search if the word "learning" exists in the file or not

with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find("learning") >= 0):
        print("It exists")
    else:
        print("It does not exist")