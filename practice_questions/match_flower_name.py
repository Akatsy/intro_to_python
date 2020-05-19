# Practice Question

# Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

# Sample Output:

# >>> Enter your First [space] Last name only: Bill Newman
# >>> Unique flower name with the first letter: Bellflower

def dict_creator(file):
    flower_dict = {}
    with open(file) as f:
        for line in f:
            line_list = line.split(':')
            flower_dict[line_list[0]] = line_list[1].strip()
    return flower_dict

def match_flower_name():
    flowers_file = '/home/mutwiri2/Desktop/intro_to_python/practice_questions/flowers.txt'
    name = input("Enter your First [space] Last name only: ")
    flower_dict = dict_creator(flowers_file)
    first_letter = name.strip()[0].upper()
    flower_name = flower_dict.get(first_letter)
    print("Unique flower name with the first letter:", flower_name)

match_flower_name()



