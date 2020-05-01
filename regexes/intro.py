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
print("You can create groups in regexes using parantheses, then you can use the Match Object group() method to grab the matching text from a particular group")
print("The first set of parantheses in a regex will be group 1, the second will be group 2 and so on...")
print("Passing the integer 1 or 2 to the Match Object's group() method will return either of the two different parts of the matched text. Passing 0 or nothing to the group() method will return the entire matched string")
phone_num_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phone_num_regex.search("My number is 415-555-4242.")
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print("#" * 99)

print("If you would like to retrieve all the groups at once, use the groups() method -- Note the plural form.")
print(mo.groups())
print("mo.groups() returns a tuple of multiple values (i.e matched text of each group). We can therefore use multiple-assignment to assign the returned values to different variables")
area_code, main_number = mo.groups()
print(f"area code is {area_code}, main number is {main_number}")


print("#" * 99)

print("The parantheses have a special meaning in regex, so if you want to match them in your text, you will need to escape them in the raw string passed to re.compile() when creating the regex object")
phone_num_regex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phone_num_regex.search("My phone number is (415) 555-4242.")
area_code, main_number = mo.groups()
print(f"area code is {area_code}, main number is {main_number}")

print("#" * 99)

print("characters with special meaning in regular expressions and how to include them".upper().center(99,'='))
SPECIAL_CHARACTERS = ('.', '^', '*', '+', '$', '?', '\\', '|', '{', '}', '[', ']', '(', ')')
for char in SPECIAL_CHARACTERS:
    print(f'Character: {char} how to include it: \{char}')


print("#" * 99)

print("matching multiple groups with the pipe".upper().center(99, '='))
print("The | is the pipe character. It can be used to match one of many expressions e.g if you have r'Kenya|Nairobi' then your regex will match Kenya or Nairobi. If there is occurrence of both in the searched string, then the first matched text will be returned.")
pipe_regex = re.compile(r'Kenya|Nairobi')
mo1 = pipe_regex.search('The capital city of Kenya is Nairobi.')
print(mo1.group())

pipe_regex = re.compile(r'Kenya|Nairobi')
mo2 = pipe_regex.search('Nairobi is the capital city of Kenya.')
print(mo2.group())

print("#" * 99)

print("You can also use pipe to match one of several patterns e.g say you want to get teams with the word city at the end e.g Manchester city, Leicester city, Norwich City etc, it would be convenient if you could be able to just specify city once in the regex. That is possible by using parantheses")
team_regex = re.compile(r'(Manchester|Leicester|Norwich|Cardiff) city')
mo = team_regex.search("The following teams are English teams: Manchester city, Manchester United, Leicester city, Norwich city, Cardiff city")
print(mo.group())
print(mo.group(1))

print("The call mo.group() returns the full matched text while mo.group(1) returns just the part of the matched text inside the group 1 (in paranthesis)")
print("By using the pipe character and grouping parantheses, you can specify several alternative patterns you would like your regex to match")

print("#" * 99)

print("optional matching with the ? character".upper().center(99, '='))
print("Sometimes, you want to match a pattern optionally e.g you might want to match a phone number with area code part being optional, i.e your regex will match a phone number with an area code and one without as well")
phone_num_regex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo1 = phone_num_regex.search("My number is 415-555-4242")
print(mo1.group())

mo2 = phone_num_regex.search("My number is 555-4242")
print(mo2.group())

print("The (group)? tells regex to match none or one occurrence of the group preceding the ? character")

print("#" * 99)

print(" matching zero or more with the * ".upper().center(99, '='))
print("The * (star or asterisk) means 'zero or more' i.e the group preceding it can occur zero, one or more than one times e.g r'Bat(wo)?man' would match Batman (no occurrence of 'wo'), Batwoman (one occurrence of 'wo') and Batwowowowowowoman (more than one occurrence of 'wo')")
heroRegex = re.compile(r'Bat(wo)?man')
mo1 = heroRegex.search("Batman (no occurrence of 'wo'), Batwoman (one occurrence of 'wo') and Batwowowowowowoman (more than one occurrence of 'wo')")
print(mo2.group())
mo2 = heroRegex.search("Batwoman (no occurrence of 'wo'), Batwoman (one occurrence of 'wo') and Batwowowowowowoman (more than one occurrence of 'wo')")
print(mo1.group())
mo3 = heroRegex.search("Batwowowowowoman (no occurrence of 'wo'), Batwoman (one occurrence of 'wo') and Batwowowowowowoman (more than one occurrence of 'wo')")
print(mo3.group())
print(mo3.group(1))

print("#" * 99)

print(" matching one or more with the + ".upper().center(99,'='))
print("You can use the + (plus) to specify that the group preceding it in the regex must appear at least once in the search text. It will match one or more occurrences.")
heroRegex = re.compile(r'Bat(wo)+man')
mo = heroRegex.search("Batwoman")
print(mo.group())
mo = heroRegex.search("Batwowowowoman")
print(mo.group())
mo = heroRegex.search("Batman")
print(mo == None)


print("#" * 99)

print(" matching specific repetitions with braces {} ".upper().center(99, '='))
print("If you have a group that you want to repeat a number of times, follow that group in your regex with a number in braces e.g (Ha){3} will match the string 'HaHaHa'")
print("Instead of a single number, you can specify a range by adding a minimum, a comma and a maximum number inside the braces e.g (Ha){3,6} will match 3, 4, 5 or 6 repetitions of the string 'Ha' ")
print("You can leave the minimum and maximum numbers out to have unbounded minimum and maximum values e.g (Ha){3,} will match 3 or more repetitions of the string 'Ha' while (Ha){,5} will match zero to five repetitions of the pattern 'Ha' ")
laugh_regex = re.compile(r'(Ha){3}')
mo = laugh_regex.search("HAhaHaHaHaHaHa")
print(mo.group())


laugh_regex = re.compile(r'(Ha){3,7}')
mo1 = laugh_regex.search("HAhaHaHaHaHaHaHAHaHaHaHaHaha")
print(mo1.group())

laugh_regex = re.compile(r'(Ha){2,}')
mo2 = laugh_regex.search("HAhaHaHaHaHaHaHAHaHaHaHaHaha")
print(mo2.group())

laugh_regex = re.compile(r'(Ha){,10}')
mo3 = laugh_regex.search("HaHaHaHaHaHaHaHAHaHaHaHaHaHaHaHaHaHaHaHaHa")
print(mo3.group())

print("#" * 99)
print("#" * 99)
print("#" * 99)
print("#" * 99)
print("#" * 99)





