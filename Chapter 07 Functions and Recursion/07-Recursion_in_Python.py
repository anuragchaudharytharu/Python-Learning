'''
    RECURSION

    When a function calls itself repeatedly. Its just like loops. All the simple task is done by loops where as recursion is used for complex task.

    All loops task can also be done by recursion and vice versa

    # Recursive Function <====> Write a program to print n to 1 backwords
            def show(n):
                if(n == 0): # Base Case
                    return
                print(n)
                show(n-1)
            show(5)

        Output =====> in order 5   4   3   2   1

    Base Case is the stopping condition of the recursive loop         
'''

# Write a program to print n to 1 backwords
def show(n):
    if(n == 0): # Base Case
        return
    print(n)
    show(n-1)
    print("End")
show(3) 
'''
    Output: 
            3
            2
            1
            End
            End
            End
'''


# Write a program to find the factorial of n
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    return factorial(n-1) * n

print(factorial(5)) # 120