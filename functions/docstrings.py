print("functions have the advantage of making code easier to understand by making it easier to read and write blocks of code")
print("functions can help break down a program into smaller chunks by implementing a singular task that is part of the whole")
print("By naming functions using descriptive names of what task they accomplish, we help in improving understanding of code")
print('#' * 99)
print("Apart from using descriptive names for functions, we can also add documentation to help other programmers and our future selves understand what a funtion does")
print("DOCSTRINGS (documentation strings) are a type of comments that describe the purpose of a function and how to use it.")
print('#' * 99)
print("DOCSTRINGs are wrapped using triple quotes(\"\"\")")
print("The first line of a docstring gives a brief description of what the function does. This is enough if he function is not that complicated")
print('#' * 99)
print("If the function is a little complicated, you can include a paragraph to further describe the function")
print("The next line after the brief description is a description of the inputs (arguments) to the function.Here you list the arguments the function will take and their expected types, Then a description of what the arguments actually are (what they represent)")
print("After the inputs description, it is good to give a description of the output of the function also (what the function returns or prints out)")
def population_density(population, land_area):
    """ Calculate the population density of an area
        INPUT:
        population: int. The number of people in an area
        land_area: int or float. This is unit-agostic meaning if you give the area in a certain unit, say kilometres or miles, the answer will be given in that unit
        OUTPUT:
        population_density: population/land_area. The population density of a given area """ 
    return population/land_area
print(population_density(900, 90))