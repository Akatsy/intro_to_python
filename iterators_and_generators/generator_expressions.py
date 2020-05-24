print(r'''

Python Generator Expressions
Simple generators can be easily created on the fly using generator expressions. It makes building generators easy.

Similar to the lambda functions which create anonymous functions, generator expressions create anonymous generator functions.

The syntax for generator expression is similar to that of a list comprehension in Python. But the square brackets are replaced with round parentheses.

The major difference between a list comprehension and a generator expression is that a list comprehension produces the entire list while the generator expression produces one item at a time.

They have lazy execution ( producing items only when asked for ). For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.

sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_generator = (x**2 for x in range(10))  # this produces an iterator of squares
This can help you save time and create efficient code!
''')

sq_list = [x**2 for x in range(100)]
print(sq_list)
sq_generator = (x**2 for x in range(100))
print(sq_generator)


print('#' * 99)

print(r'''
Generator expressions can be used as function arguments. When used in such a way, the round parentheses can be dropped.

>>> sum(x**2 for x in range(100))
328350

>>> max(x**2 for x in range(100))
9801
''')

print(sum(x**2 for x in range(100)))
print(max(x**2 for x in range(100)))

print('#' * 99)

print(r'''
A few reasons why generators are used in Python:

1. Memory Efficient
A normal function to return a sequence will create the entire sequence in memory before returning the result. This is an overkill, if the number of items in the sequence is very large.

Generator implementation of such sequences is memory friendly and is preferred since it only produces one item at a time.
A generator does not produce the required result immediately. Instead, it returns a generator object, which produces items only on demand.

2. Represent Infinite Stream
Generators are excellent mediums to represent an infinite stream of data. Infinite streams cannot be stored in memory, and since generators produce only one item at a time, they can represent an infinite stream of data.

The following generator function can generate all the even numbers (at least in theory).

def all_even():
    n = 0
    while True:
        yield n
        n += 2
''')

def all_even():
    num = 0
    while True:
        yield num
        num += 2

# try out the infinite stream with a break condition so it does not run forever
for i in all_even():
    print(i)
    if i == 100:
        break