print("Regular expressions (or regexes in short) are descriptions for a pattern of text.")
print("A regular expression specifies a set of strings (a sequence of characters) that matches it.")
print("A regex is a sequence of characters that define a search pattern")
print("For example, \d in a regex stands for a digit character i.e any single numeral character from 0-9 will match this regex")
print("#" * 99)

print("A regex defined as \d\d\d-\d\d\d-\d\d\d\d would tell Python to match a sequence of characters with 3 digits then a hyphen followed by 3 digits, another hyphen followed by 4 digits. Any text that does not match this search pattern would not be returned")
print("Regexes can be much more complicated than that e.g adding an integer in braces after a regex like \d{3} is like saying match this pattern 3 times, so the above regex shortened would be \d{3}-\d{3}-\d{4}")

print("#" * 99)

print("CREATING REGEX OBJECTS".center(66, '*'))
print("All the regex functions in Python are in the re module, so we must always import the module if we want to use regexes: >>>import re")
import re
print("Passing a string representing your regex (description of a pattern of text) to re.compile() function returns a Regular Expression pattern object or simply a regex object. ALWAYS REMEMBER TO USE A RAW STRING FOR THE REGEX")
print("For example: phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}') will return a regex object (to match a sequence of characters with 3 digits then a hyphen followed by 3 digits, another hyphen followed by 4 digits) and store it to the variable phone_num_regex")
phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')

print("#" * 99)

print("MATCHING REGEX OBJECTS".center(66, '*'))
print("A regex object's search method searches the string it is passed for a pattern matching the regex")
print("search() will return the null value None if no match is found in the string")
print("If a match is found (i.e a pattern matching the regex) then search method returns a Match Object which have a group() method that will return the actual matched text from the search string")
mo = phone_num_regex.search('Call me at 415-555-1011 tomorrow')
print("Phone number found:", mo.group())

print("#" * 99)

print("steps to using regular expressions in Python".upper().center(100, '*'))
print("1. import the regex module with >>>import re")
print("2. Create a regex object with re.compile(). REMEMBER TO USE RAW STRINGS")
print("3. Pass the string you want to search to the regex object's search method which returns a Match Object")
print("4. Call the Match Object's group() method which returns a string of the actual matched text")


print("#" * 99)

print("grouping with parantheses".upper().center(99, '*'))
print("You can create groups in regexes using parantheses, then you can use the Match Object group() method to grab the specific text for a particular group")
print("The first set of parantheses in a regex will be group 1, the second will be group 2 and so on...")
print("Passing the integer 1 or 2 to the Match Object's group method will return either of the two different parts of the matched text. Passing 0 or nothing to the group() method will return the entire matched string")
phone_num_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phone_num_regex.search("My number is 415-555-4242.")
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print("#" * 99)
print("#" * 99)
print("#" * 99)


