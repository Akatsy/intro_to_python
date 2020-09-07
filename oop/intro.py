print(r'''
Objects are a way of organizing code in a program and breaking things down to 
make it easier to think about complex ideas

Classes are a way of classifying things (objects) into groups and classes are what defines objects

We define classes using the class keyword followed by name (convention is first letter is capitalized)
e.g
class Things:
    pass

If a class is a part of another class, then it is called a child of that class and the other class is
its parent.
To tell Python that a class is part of another class, we put the name of the parent class in parantheses
after the name of our class
e.g
class Inanimate(Things):
    pass

class Mammals(Animals):
    pass
''')