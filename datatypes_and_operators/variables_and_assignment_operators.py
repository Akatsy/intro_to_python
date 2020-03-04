#Variables and assignment operators - how to store data in Python
print("Variables are a way to store data so as to access that data later. The power this brings to programming is immense")
print('#' * 79)
print("This is how to declare a variable to store data(value of any type e.g a number):")
print("variable_name = value")
print('#' * 79)
print("Whatever term is on the left(variable_name) becomes a name for whatever value is on the right. The '=' sign is what is called 'assignment operator and all it does is assigns value on the right to the name on the left. N.B: THE '=' SIGN IS NOT FOR EQUALITY!! IT DOES NOT MEAN THE NAME ON THE LEFT IS EQUAL TO THE VALUE ON THE RIGHT AND THE VALUE ON THE RIGHT IS EQUAL TO THE NAME ON THE LEFT AS THE CONVENTIONAL '=' SIGN MEANS IN MATH.")
print('#' * 79)
print("'top_student_marks = 450' assigns the value 450 to the variable top_student_marks which is self eplanatory i.e the top student had 450 marks. Once you have assigned a value to a variable, you can access that value using the variable name as shown below:")
top_student_marks = 450
print("Top student in the exam got", top_student_marks)
print('#' * 79)
print("As seen above, variable names should be representative(descriptive) of the values they hold. This is good practice and helps you avoid common pitfalls when naming variables")
print("Variable names should follow the following rules:")
print("\t1. can only contain ordinary letters, numbers and underscores - so no spaces or special characters allowed")
print("\t2. must begin with a letter or underscore, so cannot begin with a number")
print("\t3. must not be Python reserved keywords or built-in identifiers")
print("\t4. construct your variable names using snake_case i.e all lowercase and use underscores to join words - not a rule, rather a convention used by many Pythonistas. Not following this will not result in an error unlike the others above.")
print('#' * 79)
print("You can declare multiple variables at once using one expression like this:")
print("x,y,z = 4, 5.6, 8")
print("This assigns 4 to x, 5.6 to y and 8 to z")
x,y,z = 4, 5.6, 8
print("x:{} y:{} z:{}".format(x,y,x))
print("Only use multiple assignments like above for closely related data e.g co-ordinates of a point and remember variable names should be descriptive of the values they hold. The above variable names are okay, for say, co-ordinates in a 3D-axis")
print('#' * 79)
print("You can change the value of a variable once you have declared it as follows:")
print("Suppose you had declared your weight as 'weight = 56' then after a while you had it measured and found it to be 58kgs. You can change the value in two ways:")
print("1. just re-assign the new value to the variable like 'weight = 58'")
print("2. add the weight gained to the variable and then reassign it like 'weight = weight + 2'")
weight = 56
print("my weight is", weight)
weight = 58
print("my new weight after re-assigning is", weight)
weight = weight + 2
print("my new weight after adding weight gained is", weight)
print('#' * 79)
print("There are special assignment operators in python to deal with the above common use-case of performing an arithmetic operation to a variable e.g adding and then re-assigning the new value to the variable")
print("The special assignment operators are all the arithmetic operators followed by the '='(assignment operator) e.g the two most common '+=' and '-='. What they do is just apply the arithmetic operation to the variable on the left using the value on the right and then assign it back to the variable")
print('#' * 79)
print("e.g, say you have 'x=2', and you want to increase x by 2 then decrease x by 1 then multiply x by 3 then raise x to the power of 4 then do float division of x by 6 and finally integer division of x by 5 you would do the following:")
x = 2
print('x = 2 gives', x)
x += 2
print('x += 2 gives', x)
x -= 1
print('x -= 1 gives', x)
x *= 3
print('x *= 3 gives', x)
x **= 4
print('x **= 4 gives', x)
x /= 6
print('x /= 6 gives', x)
x //= 5
print('x //= 5 gives', x)
print('#' * 79)
print('Below are python keywords that cannot(read as should not- because really, you can use them but they will lead to unwanted errors eventually when you try using them for their reserved purposes in Python) be used as variable names is:')
import keyword
for index, keyword in enumerate(keyword.kwlist):
    print(index, keyword)
# print(keyword.kwlist)

print('#' * 79)
print('You can check if a word is a python keyword by typing the following on your REPL(A read–eval–print loop, also termed an interactive toplevel or language shell, is a simple, interactive computer programming environment that takes single user inputs (i.e., single expressions), evaluates (executes) them, and returns the result to the user;) and replacing "variable_name" with the name you want to check:')
print('\t1. import keyword')
print('\t2. print(keyword.iskeyword(\'variable_name\'))')
print('#' * 79)
print("As a programmer, you cannot avoid bugs or errors in your code. Errors do not make you a bad programmer-- they are just a way of the computer telling you that it does not understand what you have instructed it to do. Do not fear them, instead use them to learn to write better programs that the computer understands and executes to give the desired output")
print('#' * 79)
print("Let's generate our first error by trying to access a variable name we have not defined:")
print("The statement below 'print(my_variable)' generates an error called 'NameError' and as it states 'my_variable is not defined")
print('#' * 79)
print("An error like the one below(syntax or parsing error) forces the program to stop execution at the point of failure and exit thus any statements after are not executed")
print("Note: Python Interpreter reads and executes python code from top to bottom")
print('#' * 79)
print(my_variable)
print('Hello there!') #will not be executed because the line preceding it has a syntactic or parsing error