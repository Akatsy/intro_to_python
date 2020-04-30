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



print("#" * 99)
print("#" * 99)

