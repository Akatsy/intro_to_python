print("zip and enumerate are useful builtin functions when dealing with lists")
print("zip is a builtin function that returns an iterator which combines multiple iterables into one sequence of tuples. Each tuple contains the elements at that position from all iterables")
print('#' * 99)
letters = ['a', 'b', 'c', 'd', 'e', 'f']
numbers = [1, 2, 3, 4, 5, 6]
print("for example if you had two lists as follows:\nletters = ['a', 'b', 'c', 'd', 'e', 'f'] and \nnumbers = [1, 2, 3, 4, 5, 6] \nand you called the zip function on them and then passed the result to the list function as follows list(zip(letters, numbers)) you would get:\n {}".format(list(zip(letters, numbers))))
print('#' * 99)
print("Note that zip returns an iterator similar to the range() function so you have to call the list function on the result of zip to convert it to a list and see the results")
print("You could also just iterate through using a for loop if you want to print out the result as follows\n {} to get the result below".format("for object in zip(letters, numbers):\n\tprint(object[0], object[1])"))
for object in zip(letters, numbers):
    print(object[0], object[1])

print('#' * 99)
print("You can also unzip a list and print the elements out as follows:\n{}".format("for letter, number in zip(letters, numbers):\n\tprint(letter, number)"))
for letter, number in zip(letters, numbers):
    print(letter, number)

print('#' * 99)
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
print("The zip function can also be used to unzip a list into tuples")
print("for example, if given the following list; manifest = [(\"bananas\", 15), (\"mattresses\", 24), (\"dog kennels\", 42), (\"machine\", 120), (\"cheeses\", 5)], we can use zip to unzip the list into tuples using items, weights = zip(*manifest) to get the reult below")
items, weights = zip(*manifest)
print(items, weights)

print('#' * 79)