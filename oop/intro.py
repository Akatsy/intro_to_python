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

To create an object (also called instance of a class), we use the code snippet below
object_name = class_name()

We call the class name with parantheses at the end and assign it to a variable that will store it

To make objects more useful, we can describe characteristics of objects that belong to a class.
These characteristics can be thought of as actions, or functions — things that an object of that
class can do

When we define a function that is associated with a class, we do so in the same way that we define
any other function, except that we indent it beneath the class definition e.g

class Mammals(Animals):
    def feed_young_one_with_milk(self):
        pass

Class functions first parameter is self. The self parameter is a way for one function in the class
to call another function in the class (and in the parent class). 

Each class will be able to use the characteristics (the functions) of its parent. This means that
you don’t need to make one really complicated class; you can put your functions in the highest parent
where the characteristic applies. (This is a good way to make your classes simpler and easier to
understand.)

If we create a new object with the same variable name as an object we’ve already created, the old
object won’t necessarily vanish.

Apart from characteristics, we can also set properties (values) for objects.
To do this, we create an __init__ function (notice that there are two underscore characters on each
side, for a total of four)

This is a special type of function in Python classes and must have this name. The init function is a
way to set the properties for an object when the object is first created, and Python will
automatically call this function when we create a new object e.g

class Leopards(Mammals):
    def __init__(self, spots):
        self.spots = spots

chui = Leopards(100)
print(chui.spots)

When we create an object of a class, such as chui above, we can refer to its variables or functions
using the dot operator and the name of the variable or function we want to use (for example,
chui.spots). But when we’re creating functions inside a class, we refer to those same variables
(and other functions) using the self parameter (self.spots).
''')