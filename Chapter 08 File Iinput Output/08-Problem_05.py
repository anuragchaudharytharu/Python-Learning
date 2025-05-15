# From a file containing numbers separated by comma, print the count of even numbers. If file doesnot exist, create a file
count = 0
with open("numbers.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    print(nums)

    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)

'''
    Beginner way====> writing code from scratch
            num = ""
            for i in range(len(data)):
                if(data[i] == ","):
                    print(num)
                    num = ""
                else:
                    num += data[i]
'''  


