# Quiz: Compute an Exponent
# It's your turn to import and use the math module. Use the math module to calculate e to the power of 3. print the answer.

# Refer to the math module's documentation to find the function you need!

# # print e to the power of 3 using the math module
# import math
# print(math.exp(3))
#   
# Quiz: Password Generator
# Write a function called generate_password that selects three random words from the list of words word_list and concatenates them into a single string. Your function should not accept any arguments and should reference the global variable word_list to build the password.

# Use an import statement at the top
import random
from pathlib import Path
word_file = Path.cwd()/"practice_questions/words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    import random
    password = ''
    for i in range(3):
        password += random.choice(word_list)
    return password

def generate_password():
    return ''.join(random.sample(word_list,3))

# test your function
print(generate_password())