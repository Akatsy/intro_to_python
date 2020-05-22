# iterate (repeat an action) over an iterable using the for loop
print("loops are a way to repeat blocks of code")
print("Python has two types of loops:\n\t1. {} \n\t2. {}".format("for loops", "while loops"))
print('#' * 99)
print("for loops are loops that iterate (repeatedly do an action) over an iterable")
print("An iterable is an object that can return each of its elements one at a time")
print("An iterable can be of the sequence types like lists, tuples, strings etc or of the non-sequence types like dicts and files")
print("You can define objects with an iter method to allow them to be used as an iterable")
print('#' * 99)
print("A for loop can be defined as follows:")
print("for iteration_variable in iterable:\n\t#block of code to be executed")
print('#' * 99)
print("You begin with the for keyword which signals that this is a for loop,\nthen the iteration variable (which represents the element from the iterable that the loop is currently processing for each iteration)\nthen the in keyword (membership operator),\nthen the iterable (the object that can return each of its elements one at a time)\nFinally you end the for statement with a full colon(:)")
print('#' * 99)
print("Below the for statement is an indented block of code that executes once for each iteration")
print("The iteration variable can be accessed and used by the indented block of code during each iteration")
print('#' * 99)
print("After the body of a for loop has executed, we do not move on to the next line yet (i.e the line after the indented block). Rather, program execution goes back to the for statement where the iteration variable takes on the value of the next element from the iterable and the body is executed again.")
print("This process repeats until the for loop has iterated over all the elements of the iterable. Then now program execution moves on to the line after the indented block of code (body of the loop)")
print('#' * 99)
print("The naming convention for iteration variables and iterables is to use the same name where the iteration variable is in the singular form and the iterable is in plural form e.g 'for city in cities:'")

print('#' * 99)

print("The range() function is a useful function when dealing with loops\nIt generates an iterable immutable sequence of numbers")
print("range() returns an object that produces a sequence of integers from start (inclusive) to stop (exclusive)")
print("The range() function has three arguments, all of which must be integers as follows and of which the first and third are optional - range(start, stop, step)")
print("Start indicates which number the sequence starts from, the default is 0")
print("Stop is one number higher than the last number in the sequence- this argument is mandatory")
print("Step is the difference between each number in the sequence - defaults to one (1) if not specified")
print('#' * 99)
print("If you supply only one argument to range() then it is used as the stop value and the start defauts to 0 and step to 1")
print("If you supply two arguments to range() then the first is used as the start value and the second as the stop value and step defaults to one.")
print("If you supply three arguments to range() then the first is used as the start value, the second as the stop value and the third as the step")
print('#' * 99)
print("range() is often used to repeat a block of code a number of times e.g to print a greeting 10 times we would do it as follows;\n for i in range(10):\n\tprint('Helloooo')")
for i in range(10):
    print("Helloooo")


print('#' * 99)
# PRACTICE
teams = ['Liverpool', 'Mancity', 'Man-u', 'Arsenal', 'Tottenham']
for team in teams:
    print(team.lower()) # print out each element in teams converted to lower case
print("All Done!")

print('#' * 79)

reversed_elements_list = []
for team in teams:
    reversed_elements_list.append(team[::-1])  #  reverse each string(element) in the teams list and add it to the new list
print(reversed_elements_list)

print('#' * 79)

#modify the team list to have all caps using the range() function
for index in range(len(teams)):
    teams[index] = teams[index].upper()
print(teams)

print('#' * 79)

print(range(0, 100, 5))  # returns a range object
print(list(range(0, 100, 5)))  # convert range object to a list object
for num in range(0, 100, 5):  # iterate through the range object and print each number
    # print(num, end =" ")   #print numbers on the same line
    print(num)

print('#' * 79)
# Use a for loop to take a list and print each element of the list in its own line.
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for word in sentence:
    print(word)

print('#' * 79)

# Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.
for num in range(5,31,5):
    print(num)

print('#' * 99)

# Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:

# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# should create the list:

# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
user_names = []
for name in names:
    name = name.replace(' ', '_').lower()
    user_names.append(name)
print(user_names)

print('#' * 79)
# Write a for loop that uses range() to iterate over the positions in names to modify the list. Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores.

for index in range(len(names)):
    names[index] = names[index].replace(' ', '_').lower()
print(names)

print('#' * 79)

# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.
# tokens = ['<greeting>', 'Hello World!', '</greeting>']
# You can assume that the list of strings will not contain empty strings.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1
print("There are {} xml tags in the list of strings, tokens".format(count))

print('#' * 79)

# Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list. For example, if the list is items = ['first string', 'second string'], printing html_str should output:

# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>
items = ['first string', 'second string']
html_str = '<ul>\n'
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += '</ul>'
print(html_str)

print('#' * 79)
# create a word counter dictionary given the following string

python_history = "Python was conceived in the late 1980s[34] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC language (itself inspired by SETL),[35] capable of exception handling and interfacing with the Amoeba operating system.[8] Its implementation began in December 1989.[36] Van Rossum shouldered sole responsibility for the project, as the lead developer, until July 12, 2018, when he announced his \"permanent vacation\" from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker.[37] He now shares his leadership as a member of a five-person steering council.[38][39][40] In January, 2019, active Python core developers elected Brett Cannon, Nick Coghlan, Barry Warsaw, Carol Willing and Van Rossum to a five-member \"Steering Council\" to lead the project"

# get a list of the words in the string given and print out the list
word_list = python_history.split()
print(word_list)
print('#' * 79)

# reverse the above process. Build a string from the list of words seperated by a space then print out the string
word_string = ' '.join(word_list)
print(word_string)
print('#' * 79)

# create an empty dictionary to store the word count
word_counter = {}

# loop over every word in the list, check whether it is in the dictionary, if not add a new entry and set it to 1. If it exists increase it's count by 1

for word in word_list:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)


print('#' * 79)

# use get method to create a dictionary from a list
word_count = {}

for word in word_list:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

print('#' * 79)

# use setdefault method to create a dictionary from a list
word_count = {}

for word in word_list:
    word_count[word] = word_count.setdefault(word, 0) + 1
print(word_count)

print('#' * 79)

# check for identity and equality of the two dictionaries
print(word_count is word_counter)
print(word_counter is word_count)
print(word_count is not word_counter)
print(word_counter is not word_count)
print(word_count == word_counter)
print(word_counter != word_count)
print(word_counter == word_count)
print(word_count != word_counter)

print('#' * 99)

# iterating over dictionaries.
# 1. to get keys only and print them out
# 2. to get both keys and values and print them out
# 3. to get values only and print them out

for key in word_count.keys():
    print(key)

for key, value in word_count.items():
    print("word - {}: frequency - {}".format(key, value))

for value in word_count.values():
    print(value)


print('#' * 99)

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.


result = 0
# example 1
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
# example 2
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
# example 3
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
# example 4
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for key in basket_items.keys():
    if key in fruits:
        result += basket_items.get(key)
print(result)


# Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count = 0
not_fruit_count = 0

for key in basket_items.keys():
    if key in fruits:
        fruit_count += basket_items.get(key)
    else:
        not_fruit_count += basket_items.get(key)
print("There are {} fruits in the basket".format(fruit_count))
print("There are {} non-fruits in the basket".format(not_fruit_count))

# cleaner solution to the one above
# test example
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, count in basket_items.items():
    if object in fruits:
        fruit_count += count
    else:
        not_fruit_count += count
print("There are {} fruits in the basket".format(fruit_count))
print("There are {} non-fruits in the basket".format(not_fruit_count))

print('#' * 79)
# find the factorial of a number using for loop
number = 10
factorial = 1
for num in range(2,number+1):
    factorial *= num
print("The factorial of {} is {}".format(number, factorial))