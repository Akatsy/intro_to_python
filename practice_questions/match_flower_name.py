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
    print(flower_dict)

flowers_file = '/home/mutwiri2/Desktop/intro_to_python/practice_questions/flowers.txt'
dict_creator('flowers.txt')

