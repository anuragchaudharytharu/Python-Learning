# Write a recursive function to print all elements in a list. HINT: use list & index as parameters

fruits = ["mango", "litchi", "apple", "banana"]
def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx + 1)

print_list(fruits)