print(r'''
There are tens of thousands of third-party libraries written by independent
developers! You can install them using pip, a package manager that is included
with Python 3. pip is the standard package manager for Python, but it isn't the
only one. One popular alternative is Anaconda which is designed specifically
for data science.

To install a package using pip, just enter "pip install" followed by the name of
the package in your command line like this: pip install package_name. This
downloads and installs the package so that it's available to import in your
programs. Once installed, you can import third-party packages using the same
syntax used to import from the standard library.

Larger Python programs might depend on dozens of third party packages. To make
it easier to share these programs, programmers often list a project's
dependencies in a file called requirements.txt. This is an example of a
requirements.txt file.

beautifulsoup4==4.5.1
bs4==0.0.1
pytz==2016.7
requests==2.11.1

Each line of the file includes the name of a package and its version number.
The version number is optional, but it usually should be included. Libraries can
change subtly, or dramatically, between versions, so it's important to use the
same library versions that the program's author used when they wrote the program.

You can use pip to install all of a project's dependencies at once by typing
"pip install -r requirements.txt" in your command line.

Python comes with batteries-included means Python comes with the libraries you
need to get right to work

Put import statements for 3rd party libraries after import statements from the
standard library 
''')

print('#' * 99)

print(r'''
Useful Third-Party Packages
Being able to install and import third party libraries is useful, but to be an
effective programmer you also need to know what libraries are available for you
to use. Here are a few examples:

IPython - A better interactive Python interpreter

requests - Provides easy to use methods to make web requests. Useful for
accessing web APIs.

Flask - a lightweight framework for making web applications and APIs.

Django - A more featureful framework for making web applications. Django is
particularly good for designing complex, content heavy, web applications.

Beautiful Soup - Used to parse HTML and extract information from it. Great for
web scraping.

pytest - extends Python's builtin assertions and unittest module.

PyYAML - For reading and writing YAML files.

NumPy - The fundamental package for scientific computing with Python. It contains
among other things a powerful N-dimensional array object and useful linear
algebra capabilities.

pandas - A library containing high-performance, data structures and data analysis
tools. In particular, pandas provides dataframes!

matplotlib - a 2D plotting library which produces publication quality figures in
a variety of hardcopy formats and interactive environments.

ggplot - Another 2D plotting library, based on R's ggplot2 library.

Pillow - The Python Imaging Library adds image processing capabilities to your
Python interpreter.

pyglet - A cross-platform application framework intended for game development.

Pygame - A set of Python modules designed for writing games.

pytz - World Timezone Definitions for Python

''')

print('#' * 99)

print(r'''
Getting the information you need to know
It takes an enormous amount of knowledge to be a skilled programmer. There's
libraries to know, syntax to remember, and myriad other details. To add to the
difficulty, the technology landscape is constantly shifting as new techniques
and tools are invented.

To a novice programmer, learning all of these details and keeping abreast of new
developments seems like an impossible task. And it is! Expert programmers who
have been working for years don't actually carry an encyclopedia's worth of
knowledge in their heads. Instead they have mastered the task of finding
information quickly.

How to Search
Here are some techniques for effective web searching:

Try using "Python" or the name of the library you're using as the first word of
your query. This tells the search engine to prioritize results that are explicitly
related to the tools you're using.

Writing a good search query can take multiple attempts. If you don't find helpful
results on your first attempt, try again.
Try using keywords found on the pages you found in your initial search to direct
the search engine to better resources in the subsequent search.

Copy and paste error messages to use as search terms. This will lead you to
explanations of the error and potential causes. An error message might include
references to specific line numbers of code that you wrote. Only include the part
of the error message that comes before this in your search.

If you can't find an answer to your question, ask it yourself! Communities like
StackOverflow have etiquette rules you must learn if you want to participate,
but don't let this stop you from using these resources.
''')

print('#' * 99)

print(r'''
Hierarchy of Online Resources
While there are many online resources about programming, not all of the them are
created equal. This list of resources is in approximate order of reliability.

1. The Python Tutorial - This section of the official documentation surveys
Python's syntax and standard library. It uses examples, and is written using
less technical language than the main documentation. Make sure you're reading
the Python 3 version of the docs!

2. The Python Language and Library References - The Language Reference and
Library Reference are more technical than the tutorial, but they are the
definitive sources of truth. As you become increasingly acquainted with Python
you should use these resources more and more.

3. Third-Party Library Documentation - Third-party libraries publish their
documentation on their own websites, and often times at https://readthedocs.org/.
You can judge the quality of a third-party library by the quality of its
documentation. If the developers haven't found time to write good docs, they
probably haven't found the time to polish their library either.

4. The websites and blogs of prominent experts - The previous resources are
primary sources, meaning that they are documentation from the same people who
wrote the code being documented. Primary sources are the most reliable. Secondary
sources are also extremely valuable. The difficulty with secondary sources is
determining the credibility of the source. The websites of authors like Doug Hellmann
and developers like Eli Bendersky are excellent. The blog of an unknown author
might be excellent, or it might be rubbish.

5. StackOverflow - This question and answer site has a good amount of traffic,
so it's likely that someone has asked (and someone has answered) a related
question before! However, answers are provided by volunteers and vary in quality.
Always understand solutions before putting them into your program. One line
answers without any explanation are dubious. This is a good place to find out
more about your question or discover alternative search terms.

6. Bug Trackers - Sometimes you'll encounter a problem so rare, or so new, that
no one has addressed it on StackOverflow. You might find a reference to your
error in a bug report on GitHub for instance. These bug reports can be helpful,
but you'll probably have to do some original engineering work to solve the problem.

7. Random Web Forums - Sometimes your search yields references to forums that
haven't been active since 2004, or some similarly ancient time. If these are
the only resources that address your problem, you should rethink how you're 
approaching your solution.
''')
