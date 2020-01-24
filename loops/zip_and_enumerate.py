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

print("enumerate() is a function that returns an iterator of tuples containing indices and values of a list")
print('#' * 99)
teams = ['Liverpool', 'Mancity', 'Leicester', 'Chelsea']
print("for example if you had a list like teams = ['Liverpool', 'Mancity', 'Leicester', 'Chelsea'] and you wanted to get a list of tuples of team and it's index, you could do the following; print(list(enumerate(teams))) to get the following output:\n{}".format(list(enumerate(teams))))
print('#' * 99)
print("You could also print out the values of a list with their indices using enumerate as follows:\n for i, letter in enumerate(teams):\n\tprint(i, letter)\nto get the following output:")
for i, letter in enumerate(teams):
    print(i, letter)

print("You will often use enumerate() when you need the indices and values of a list in a loop")

print('#' * 99)
# quiz
# Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points. Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for object in zip(labels,x_coord,y_coord,z_coord):
    object = object[0] + ': ' + str(object[1]) + ', ' + str(object[2]) + ', ' + str(object[3])
    points.append(object)
    


for point in points:
    print(point)

# more succint solution
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

print('#' * 99)
# Use zip to create a dictionary cast that uses names as keys and heights as values.
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)