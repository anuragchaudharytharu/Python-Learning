# .append(element) =====> adds one element at the end of the list. It mutates the original Lists
list = [1,2,3]
list.append(4)
print(list) # [1, 2, 3, 4]




# .sort() ======> sorts in ascending order. It mutates the original Lists
a = ["b", "c", "a", "d"]
a.sort()
print(a) # ['a', 'b', 'c', 'd']




# .sort(reverse = True) ======> sorts in reverse order i.e in descending order. It mutates the original Lists
b = [2, 1, 4, 3]
b.sort(reverse = True)
print(b) # [4, 3, 2, 1]

fruits = ["banana", "litchi", "apple"]
fruits.sort(reverse = True)
print(fruits) # ['litchi', 'banana', 'apple']




# .reverse() =======> reverse the elements of the Lists. It mutates the original Lists
random = ["apple", 10, "c", 2, "d", "banana"]
random.reverse()
print(random) # ['banana', 'd', 2, 'c', 10, 'apple']




# .insert(index, element) ======> insert/add element at specified index position. It mutates the original Lists
vegetables = ["carrot", "brinjal", "onion", "cabbage"]
vegetables.insert(2, "potato")
print(vegetables) # ['carrot', 'brinjal', 'potato', 'onion', 'cabbage']




# .remove(element) =======> remove first occurances of element in the Lists. It mutates the original Lists
data = ["name", "population","cast", "religion", "population", "municipality"]
data.remove("population")
print(data) # ['name', 'cast', 'religion', 'population', 'municipality']




# .pop(index) ======> removes element from a specified index position. It mutates the original Lists
num = [2, 10, 3, 1, 10, 5, 8, 6]
num.pop(4)
print(num) # [2, 10, 3, 1, 5, 8, 6]