'''
    List Slicing ====>  same as string slicing

    lis_name[startingIndex : endingIndex] ====> endingIndex is not included inside the output result

    Rules:-
    [ : ] =====> startingIndex = 0 & endingIndex = length of the List
    [ : 5] ======> startingIndex = 0 & endingIndex = 5
    [2 : ] ======> startingIndex = 2 & endingIndex = length of the List
'''

marks = [87,64,33,95,76]

print(marks[1 : 4]) # [64, 33, 95]
print(marks[ : 4]) # [87, 64, 33, 95] i.e same as marks[0 : 4]
print(marks[2 : ]) # [33, 95, 76] i.e same as marks[2 : len(marks)]
print(marks[ : ]) # [87,64,33,95,76] i.e same as marks[0 : len(marks)]
print(marks[-3, -1]) # [33, 95] i.e same as marks[2 : lastIndex]