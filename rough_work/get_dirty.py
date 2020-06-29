tab = '    '
print("If you declare a variable tab and assign to it one tab from the keyboard\
 then len(tab) returns",len(tab))
print('#'*79)

tab_2 = '       '
print("If you declare a variable tab_2 and assign to it two tabs from the\
 keyboard then len(tab_2) returns",len(tab_2))
print('#'*79)

tab_3 = '           '
print("If you declare a variable tab_3 and assign to it three tabs from the\
 keyboard then len(tab_3) returns",len(tab_3))
print('#'*79)

newline = '''
'''
print("If you declare a variable newline and assign to it a multiline string\
 like below\nnewline = '''\n'''\n then len(newline) will return ",len(newline))
print('#'*79)

print("len('\\t') returns",len('\t'))

print("len('\\n') returns",len('\n'))

print("len(' ') returns",len(' '))
print('#' * 99)

my_list = [1,2,3]
my_list[3:6] = [4,5,6]
print(my_list)

print('#' * 99)

# what happens when you use zip on iterables of different length?
print(list(zip(['a','b','c','d'],[1,2,3])))
for letter, number in zip(['a','b','c','d'],[1,2,3]):
    print(letter, number)

print('#' * 99)
# floats store approximations not exact values
print(0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1)

# the escape character
rand_str = "Hey there, how y\\\"all doing?"
print(rand_str)

print('#'*79)
# join() method
my_list = ['a', 'b', 'c', 'd']
joined = ''.join(my_list)
print(joined)
# print(joined.split('')) - you cannot use an empty seperator for the split method

print('#'*79)
# loop over a set (iterable of non-sequence type)
for i in {1,2,3,3,4,5,6,6,8,8,9,9,9,9,10}:
    print(i)

print('#'*79)
# enumerate
print(list(enumerate('abcdefghijklmnopqrstuvwxyz', start=1)))
print('#'*79)
himym = ('Barney', 'Robin', 'Ted', 'Lily', 'Marshall')
print(enumerate(himym))
print(tuple(enumerate(himym)))
print(list(enumerate(himym)))
print(dict(enumerate(himym)))

print('#' * 99)
# dict() method on zip
my_dict = dict(zip([1,2,3,4],['a','b','c','d']))
print(my_dict)

print('#' * 99)

# keyword arguments
print("Hello", end='')
print("World")
print("World")

print("eggs", "bacon", "milk", sep='\t')

print('#' * 99)
 # The call stack
def a():
    print('a() begins')
    b()
    d()
    print('a() returns')

def b():
    print("b() begins")
    c()
    print("b() returns")

def c():
    print("c() begins")
    print("c() returns")

def d():
    print("d() begins")
    print("d() returns")

a() # call function a() to see the call stack in action

print('#' * 99)
print("What is the difference between an expression and a statement?")
print("A statement is a complete line of Python code that performs some action\
 e.g assignment statement assigns a value to a variable (initializes a variable)\
\nwhile an expression is the most basic kind of instruction in Python that is\
 made up of values and operators (or function calls) and always reduces\
 (evaluates) to a single value. An expression can be used anywhere in Python\
 where we would use a value since it always reduces to a single value")

print('#' * 99)
