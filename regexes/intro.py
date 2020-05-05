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

print("greedy and non-greedy matching".upper().center(99, '='))
print("Python's Regular expressions are greedy by default, which means given an ambigous situation, they will return the longest string possible e.g r'(Ha){3,5}' will match 3,4 or 5 repetitions of the string 'Ha' so if the search string 'HaHaHaHaHa' is the search string, Match Object's group() method will return the 5 repetitions text instead of the shorter 3 or 4 repetitions which are also valid. ")
print("The non-greedy or lazy version of the braces which matches the shortest string possible has the closing brace followed by a question mark")
greedy_ha_regex = re.compile(r'(Ha){3,5}')
mo1 = greedy_ha_regex.search('HaHaHaHaHa')
print(mo1.group())

non_greedy_ha_regex = re.compile(r'(Ha){3,5}?')
mo2 = non_greedy_ha_regex.search('HaHaHaHaHa')
print(mo2.group())

print("#" * 99)

print("the findall() method".center(99, '='))
print("Regex objects have a findall() method in addition to the search() method. The search() method returns a Match Object which contains the first occurrence of the matched text")
print("The findall() method on the other hand will return all occurrences of matched text as follows:")
print("1. If the regex does not contain groups, then findall() returns a list of strings of all matched text")
print("2. If the regex contains groups, findall() returns a list of tuples of strings. Each tuple contains strings, one for each group")

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
result = phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
result = phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)

print("#" * 99)

print("The ? character can have two meanings in regexes, which are completely unrelated:")
print("1. Declaring a non-greedy (lazy) match")
print("2. Flagging an optional group")

print("#" * 99)

print("character classes".upper().center(99, '='))
print("Character classes are nice for shortening regexes e.g \d stands for any numeric digit from 0-9 thus is a shorthand for the regex (0|1|2|3|4|5|6|7|8|9)")
print("The following are shorthand codes for common character classes:\n")
SHORTHAND_CODES = {
    r'\d': 'Any numeric digit from 0-9',
    r'\D': 'Any character that is not a numeric digit from 0-9',
    r'\w': 'Any letter, numeric digit or the underscore character',
    r'\W': 'Any character that is not a letter, numeric digit or the underscore character',
    r'\s': 'Any whitespace character i.e space, tab or newline',
    r'\S': 'Any character that is not a whitespace character'
}

sorted_values = sorted(list(SHORTHAND_CODES.values()))
right_width = len(sorted_values)
left_width = 5
for code, description in SHORTHAND_CODES.items():
    print(code.ljust(left_width) + description.rjust(right_width))

print("\nWhile \d matches digits and \w matches any letter, digit and the underscore, there is no shorthand character class that matches letters only. (though you can use the character class [a-zA-Z])")  

print("#" * 99)

sample_regex = re.compile(r'\d+\s\w+')
matched = sample_regex.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge tring built from groups 1, 3, 5, and 8 of the matched text")
print(matched)


print("#" * 99)

print("creating character classes".upper().center(99, '='))
print("Using square brackets, we can create our own character classes when the existing ones are too broad for the pattern we want to define")
vowel_regex = re.compile(r'[aeiouAEIOU]')
matches = vowel_regex.findall("The quick brown fox jumped over the lazy dog. Those Quick brown foxes Jumped over those lazy DOGS")
print(matches)

print("#" * 99)

print("We can define a range of characters using the hyphen e.g a character class like [a-zA-Z0-9] would match all letters both lowercase and uppercase from a to z and digits from 0 to 9")
letters_regex = re.compile(r'[a-zA-Z]')
matched_list = letters_regex.findall('This with keyword allows you to open a file, do operations on it, and automatically close it after the indented code is executed, in this case, reading from the file.')
print(matched_list)

print("#" * 99)

print("You can make a negative character class by placing a caret symbol (^) after the character class' opening square bracket")
print("A negative character class will match all characters that are not in the character class")
consonants_regex = re.compile(r'[^aeiouAEIOU\s\W\d]')
matched = consonants_regex.findall("This with keyword allows you to open a file, do operations on it, and automatically close it after the indented code is executed, in this case, reading from the file.")
print(matched)

print("#" * 99)

print("note that inside the square brackets, the normal special symbols / characters are not interpreted as such meaning you do not have to escape them e.g [0-5.] would match any digit from 0 to 5 and the period character (.) you do not need to escape it like [0-5\.]")

print("#" * 99)

print("the caret (^) and dollar sign ($) in regexes".upper().center(99, '='))
print("You can place the caret symbol (^) at the beginning of a regex to indicate that a match must occur at the begining of the searched text")
print("Conversely, you can place a dollar sign ($) at the end of a regex to indicate that the searched text must end with that pattern")
begins_with_vowel = re.compile(r'^[aeiouAEIOU]')
print(begins_with_vowel.search("The quick brown fox jumped over the lazy dog"))
print(begins_with_vowel.search("One is never enough"))

ends_with_fullstop = re.compile(r'\.$')
print(ends_with_fullstop.search("Be consistent."))
print(ends_with_fullstop.search("Be consistent!"))

print("#" * 99)

print("You can use both to indicate that the entire string must match the pattern i.e it is not just enough that some subset of the string matches the pattern")
begins_ends_with_number = re.compile(r'^\d+$')
print(begins_ends_with_number.search("12345676435"))
print(begins_ends_with_number.search("12345abc435"))
print(begins_ends_with_number.search("123 45676435"))

print("the entire string must match the regex if ^ and $ are used")

print("#" * 99)

print(" the wildcard character (.) ".upper().center(99, '='))
print("The period (.) is a wildcard character in regexes and will match any character except the newline character")
print("The dot character (period) will match only one character. To match an actual period you will have to escape with a backslash")
end_with_at_regex = re.compile(r'.at')
print(end_with_at_regex.findall("cat is rat but bat ain't flat are you fat big braat"))

# a four letter word starting with a ending with s
word_regex = re.compile(r'a..s')
print(word_regex.findall("glass bass asss class floss boss ares aire args argv abs"))

print("#" * 99)

print(" matching everything with dot-star (.*) ".upper().center(99, '='))
print("Remember dot-character (.) means any character except the newline character and star-character (*) means zero or more of the preceding character. Therefore we can combine both to get the dot-star character which will match anything and everything")
name_regex = re.compile(r'First Name:(.*)Last Name:(.*)')
mo = name_regex.search("First Name: Mutwiri Last Name: Mwenda")
print(mo.group())
print(mo.group(1))
print(mo.group(2))

print("#" * 99)

print("dot-star uses greedy mode by default i.e it will always try to match as much text as possible.")
print("To match anything and everything in a non-greedy mode, use the dot, star and question mark.")
greedy_regex = re.compile(r'<.*>')
mo = greedy_regex.search("<p class=\"main\"><em>lorem ipsum</em></p>")
print(mo.group())

non_greedy_regex = re.compile(r'<.*?>')
mo = non_greedy_regex.search("<p class=\"main\"><em>lorem ipsum</em></p>")
print(mo.group())

print("#" * 99)

print("matching newline character with dot-character".upper().center(99, '='))
print("the dot-character (.) matches any character except the newline character. By passing re.DOTALL as the second argument to re.compile(), you can make the dot-character match all characters including the newline")
non_newline_regex = re.compile('.*')
mo = non_newline_regex.search("YOLO\nCarpe Diem\nThe world is your oyster.")
print(mo.group())

newline_regex = re.compile('.*', re.DOTALL)
mo = newline_regex.search("YOLO\nCarpe Diem\nThe world is your oyster.")
print(mo.group())

print("#" * 99)

print("Regex symbols cheatsheet".upper().center(99, '='))
print("The ? matches zero or one of the preceding group\n")
print("The * matches zero or more of the preceding group\n")
print("The + matches one or one of the preceding group\n")
print("The {n} matches exactly n of the preceding group\n")
print("The {n,} matches n or more of the preceding group\n")
print("The {,m} matches 0 to m of the preceding group\n")
print("The {n,m} matches at least n and at most m of the preceding group\n")
print("{n,m}?, *?, +? performs a non-greedy search of the preceding group\n")
print("^spam means the searched string must begin with spam\n")
print("spam$ means the searched string must end with spam\n")
print("The . matches any character except the newline character\n")
print("\\d, \\w, \\s matches a digit, word and space characters respectively\n")
print("\\D, \\W, \\S matches anything except a digit, word or space characters respectively\n")
print("[abc] matches any character between the brackets i.e a,b or c\n")
print("[^abc] matches any character that is not between the brackets\n")

print("#" * 99)

print("case-insensitive matching".upper().center(99, '='))
print("Normally, regexes match text with the exact casing you specify. Sometimes however, you might want to match text without worrying whether they are uppercase or lowercase")
print("To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as your second parameter to re.compile()")
ignore_case_regex = re.compile(r'python',re.IGNORECASE)
print(ignore_case_regex.findall("Python pYthon, python, PYThon, PytHON"))

ignore_case_regex = re.compile(r'python',re.I)
print(ignore_case_regex.findall("Python pYthon, python, PYThon, PytHON"))

print("#" * 99)

print("substituting strings with the sub() method".upper().center(99, '='))
print("Regexes can not only find string pattern matches but can substitute those string matches. The regex object's sub() method is used to substitute string matches to the regex")
print("sub() method is passed two arguments. The first is the string to be substituted for every match and the second is the search string for the regular expression")
print("sub() returns a string with the substitution applied")
secret_agents_regex = re.compile(r'Agent \w+', re.I)
print(secret_agents_regex.sub('Censored', 'Agent Sameen fell in love with agent Root, Agent Reese fell in love with Agent Carter'))

print("#" * 99)

print("Sometimes, you might want to use the matched text itself as part of the substitution.")
print("In the first argument of sub i.e the replacement text, you can use \\1, \\2, \\3 and so on to mean that use the text in group 1, group 2, group 3 and so on of the matched text in the substitution")
secret_agent_regex = re.compile(r'(Agent) (\w)\w*', re.IGNORECASE)
censored_text = secret_agent_regex.sub(r'\1 \2****', 'Agent Sameen fell in love with agent Root, Agent Reese fell in love with Agent Carter')
print(censored_text)

print("#" * 99)

print("managing complex regexes".upper().center(99, '='))
print("Sometimes matching complicated text patterns might require long complicated regexes")
print("You can use the 'verbose method' to define this text patterns in a legible way. The verbose method tells the re.compile() function to ignore whitespaces and comments inside the regex string")
print("Pass re.VERBOSE variable as the second argument to re.compile() to enable the verbose method")
phone_regex = 

print("#" * 99)
print("#" * 99)
print("#" * 99)




