# generator functions and iterators

print(r'''
Iterables are objects that can return each of their elements one at a time e.g a list
Iterator is an object that represents a stream of data for example one returned by the enumerate function
An iterator is different from an iterable like a list since a list is not a stream of data

You can create iterators using generators
Generator - a function that creates an iterator

Generator is a simple way to create iterators using functions
Generator is often used to refer to the generator function but is sometimes also used to refer to the iterator object produced by the function

def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

The above represents a generator function called my_range that produces a stream of numbers from 0 to x-1
Note that instead of using return keyword, we use yield
''')