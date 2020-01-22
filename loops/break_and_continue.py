print("for loops iterate over every element in a sequence and while loops continue with iterations until their stop condition is met. This is how we choose where to use the two depending on the kind of functionality we aim to get")
print("However, sometimes we need to have more precise control over when our loops stop")
print("This is where the 'break' keyword comes in. break will terminate a for or while loop whenever encountered")
print('#' * 99)
print("Suppose you want to load a ship with a list of items called manifest which contains tuples as elements each with the name of an item and it's weight. Ideally, you would want to load all items to the ship but the ship has a weight limit which you should not exceed. So you need to load the items whilst checking that the weight has not been exceeded and if it has, you need to stop loading( stop the loop)")
print('#' * 99)

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
weight = 0
items = []
weight_limit = 100
for cargo in manifest:
    print("current weight is {}".format(weight))
    if weight >= weight_limit:
        print("terminating loop now...")
        break
    else:
        print("adding {} weight of {} now".format(cargo[0], cargo[1]))
        items.append(cargo[0])
        weight += cargo[1]
print("current weight ({}) and items loaded {}".format(weight, items))
print('#' * 99)

print("Sometimes, we also might need to skip an iteration because of some condition. Here we use the continue keyword")
print("continue skips an iteration of a loop")
print("Suppose, for example we had a basket of food and wanted to add only those that are fruits to another basket. Looping through the list of food, if we encounter a non-fruit, we are to skip it and not add it to our fruits list then continue looping if there are more food items")
print('#' * 99)
fruits = ['apple', 'orange', 'mango', 'pear']
food = ['cake', 'apple', 'bread', 'pear', 'juice', 'orange', 'beef', 'mango']
basket = []
for item in food:
    if item not in fruits:
        print("Not a fruit, skipping...")
        continue
    else:
        print("Found a fruit, adding to basket...")
        basket.append(item)
print("our basket contains {}".format(basket))