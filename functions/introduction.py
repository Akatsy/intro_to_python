print("Functions are useful chunks of code that let us encapsulate a task")
print("Encapsulation is a way to perform a whole series of steps using a single command")
print("In programming, functions encapsulate all the steps of a process into one command")
print('#' * 99)
print("for example suppose we want to find the volume of a cylinder, then we can define a function like:\ndef volume_cylinder(height, radius):\n\tpi = 3.14159265359\n\tvolume = pi * radius **2 * height\n\treturn volume")
def volume_cylinder(height, radius):
    pi = 3.14159265359
    volume = pi * radius **2 * height
    return volume
print('#' * 99)
print("Defining a function is as easy as above. It has a few parts as follows:")
print("1. 'def' keyword- A function definition always begins with the def keyword. This tells Python that whatever follows is a function definition. That statement that starts with def keyword must always end with a colon (:)")
print('#' * 99)
print("2. function name- Immediately after the def keyword, what follows is the name of the function. This is the command we will call to run the code encapsulated in it. The rules for naming a function are similar to those of naming Python variables")

print('#' * 99)
print("3. After the function name is a parantheses that houses any number of arguments for the function. Arguments are variables that the function will use in it's body to generate output. Arguments are not mandatory and a function can have none. In this case, the parantheses is left blank")

print('#' * 99)
print("4. After the definition statement that ends with a colon, comes the body of the function which must be indented below it. The body can contain other variable declarations and any number of code blocks to perform a task")

print('#' * 99)
print("Then once you have declared a function, you can call it (use it) by calling the name of the function and passing in the required arguments in the parantheses e.g\nprint(volume_cylinder(45, 450))")
print(volume_cylinder(45, 450))