'''
    BREAK & CONTINUE

    BREAK ====> used to terminate the loop when encountered

    CONTINUE =====> terminates execution in the current iteration and skips the code execution after continue but continues execution of the loop with the next iteration
'''

i = 1
while i <= 5:
    if(i == 3):
        print(i)
        break
    i += 1
print("End of the Loop")    


nums = [1, 4, 9, 16, 25 ,36 ,49, 64, 81, 100, 36]
x = 36
i = 0
while i <= len(nums) - 1: 
    if(nums[i] == x):
        print(f"Found the first occurance of x = 36 at index {i}")
        break
    else:
        print("finding.....")
    i += 1  
print("End of the Loop")    


i = 0
while i <= 5:
    if (i == 3):
        i += 1
        continue
    print(i) # it skips printing 3 i.e it prints 1 to 5 except 3
    i += 1
print("End of the Loop") 
