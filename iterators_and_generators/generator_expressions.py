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