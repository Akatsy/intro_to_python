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

yield allows the function to return values one at a time and start where it left off each time it is called
the yield keyword is what differentiates a generator from a typical function

>>>print(my_range(4))
    <generator object my_range at 0x...>

Calling the generator function returns an iterator object as shown above that we can iterate through

for n in my_range(4):
    print(n)

Using a for loop we can print values from this stream of data (iterator)

''')

def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

print(my_range(4))

for n in my_range(4):
    print(n)


print(r'''
Why Generators?
https://softwareengineering.stackexchange.com/questions/290231/when-should-i-use-a-generator-and-when-a-list-in-python/290235
Generators are a lazy way to build iterables. They are useful when the fully realized list would not fit in memory, or when the cost to calculate each list element is high and you want to do it as late as possible. But they can only be iterated over once.
''')