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
print('#' * 99)

# solve the manifest bugs using continue
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
weight = 0
items = []
weight_limit = 100
for cargo_item, cargo_weight in manifest:
    if weight >= weight_limit:
        print("weight limit reached, loading stopped")
        break
    elif weight + cargo_weight > weight_limit:
        print("adding item {}, weight {} will exceed the weight limit of {}, skipping item...".format(cargo_item, cargo_weight, weight_limit))
        continue
    else:
        print("adding {} weight {} to ship".format(cargo_item, cargo_weight))
        items.append(cargo_item)
        weight += cargo_weight
print("Items addded to ship are {}, total weight of items is {}".format(items, weight))

print('#' * 99)

# Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""

for headline in headlines:
    if len(news_ticker) >= 140:
        print("140 character limit reached...")
        break
    elif len(headline) + 1 + len(news_ticker) > 140:
        print("adding the headline will exceed the character limit by {}, truncating to fit...".format(len(headline) + 1 + len(news_ticker) - 140))
        headline = headline[:140 - len(news_ticker)]
        news_ticker += headline
    else:
        news_ticker += headline + ' '
print("our news ticker is '{}' and is ({}) characters long".format(news_ticker, len(news_ticker)))

print('#' * 99)
# better solution - more succint
headlines = ["Red Hat Enterprise Linux 8.2 Beta Released With New Features",
             "ProtonVPN goes open source to build trust",
             "Python’s Execution Time Is Close To C++ And Go Language: Study",
             "Safaricom needs to fix M-Pesa privacy problems",
             "Why is Samsung jumping from Galaxy S10 to Galaxy S20?",
             "Have You Tried Kaisen Linux? — A New System Rescue Linux Distro"
]
news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 280:
        news_ticker = news_ticker[:280]
        break
print("Our newsticker is \"{}\" and has {} characters".format(news_ticker, len(news_ticker)))