'''
    WHILE Loop =====> Its mainly used when we have needs of iterators and to update the variable value

            while condition:
                #some work
                #increament/decreament
'''

count = 1 # iterator
while count <= 5 : #stopping condition
    print("Helllo") # it prints Hello five times on different lines
    count +=1
print(count) # 6 


i = 100
while i > 0 :
    print(i) # prits number from 100 to 1 
    i -= 1
print("Loop Ended At Iteration", i) # Loop Ended At Iteration 1 


nums = [1, 4, 9, 16, 25 ,36 ,49, 64, 81, 100, 36]
x = 36
i = 0
while i <= len(nums) - 1: 
    if(nums[i] == x):
        print("Found at index", i)
    else:
        print("finding.....")
    i += 1    