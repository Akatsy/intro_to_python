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
    if weight >= weight_limit:
        break
    else:
        items.append(cargo[0])
        weight += cargo[1]
print(weight)
print(items)
