'''
    range()

    Range function returns a sequence of numbers, starting from 0 by default, and increaments by 1 (by default), and stops before a specified number
            
            range(start?, stop?, step?)
    
    By default:
        start = 0
        step size = +1
'''

print(range(5)) # output: range(0, 5). This is same as range(0, 5, 1)

seq = range(5) # range(stop) i.e same as range(0, 5, 1)
print(seq[0], seq[1], seq[2], seq[3]) # 0 1 2 3

for el in range(5): # range(stop) i.e same as range(0, 5, 1)
    print(el) # prints 0 to 4

for el in range(1, 5): # range(start, stop) same as range(1, 5, 1)
    print(el) # prints 1 to 4

for el in range(1, 5, 2): # range(start, stop, step)
    print(el) # prints 1 and 3 