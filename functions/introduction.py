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

print("Then once you have declared a function, you can call it (use it) by using the name of the function and passing in the required arguments in the parantheses e.g\nprint(volume_cylinder(45, 450))")
print(volume_cylinder(45, 450))

print('#' * 99)
print("Defining a function is as easy as above. It has a few important parts as follows:")
print("A. Function header - This is the first statement in a function definition. It consists of;")
print("1. 'def' keyword- A function definition always begins with the def keyword. This tells Python that whatever follows is a function definition. That statement that starts with def keyword must always end with a colon (:)")
print('#' * 99)
print("2. function name- After the def keyword, what follows is the name of the function. This is the command we will call to run the code encapsulated in it. The rules for naming a function are similar to those of naming Python variables.")

print('#' * 99)
print("3. Immediately after the function name is a parantheses that houses any number of arguments for the function. Arguments are variables that the function will use in it's body to generate output. They are the inputs that the function will accept when called. Arguments are not mandatory and a function can have none. In this case, the parantheses is left blank")

print('#' * 99)
print("B. Function body - This is the indented block of code below the function header")
print("4. After the definition statement that ends with a colon, comes the body of the function which must be indented below it. It is where the function does it's work. The body can contain other variable declarations and any number of statements or code blocks to perform a task")
print('#' * 99)
print("An example of a function without arguments\ndef greetings():\n\tprint(\"Hello! hey! alloha!\")\n")

def greetings():
    print("Hello! hey! alloha!")

print('#' * 99)
print("calling the function as follows\nprint(greetings()) we get the output:")
print(greetings())

print('#' * 99)
print("We get back the code block inside the function body and the None keyword. Why is the None keyword given as an output?")

print('#' * 99)
print("Often, the body of a Python function will have the return keyword followed by an expression whose value is what return will give as the output value of the function. So the return keyword is used by  a function to give an output value from the function")
print("If the return keyword is not used in a function body explicitly to define the output, then the function returns None keyword as seen from the example above")

print('#' * 99)
print("When defining a function, you can provide default arguments.\nThis means giving a value to the argument which will be used as the default value if when calling a function the user does not specify a value for that argument")
print('#' * 99)

print("For example in our cylinder volume function, we can include a radius default argument as follows:")
print("def volume_cylinder(height, radius=7):\n\tpi = 3.14159265359\n\treturn pi * radius **2 * height")
print('#' * 99)
print("Default arguments are useful when we want to be more conscise with our code in scenarios where there is a commonly used value for an argument but we still want it to be customizable.")
print("If the user when calling the function, supplies a value for the default argument parameter, then the user's argument will override the default argument")

print('#' * 99)
print("There are two ways to supply arguments to a function:")
print("1. positional arguments- This is where we give values inside the parantheses that match the order of the defined arguments i.e if the first argument was height and second was radius then we specify them in that same order when calling the function e.g cylinder_volume(10, 6) so the height will be 10 and radius will be 6")
print('#' * 99)

print("2. named arguments- This is where we give values inside the parantheses using their argument names and then supply a value e.g cylinder_volume(radius=10, height=6) so the height will be 6 and radius will be 10")