tab = '    '
print(len(tab))
newline = '''
'''
print(len(newline))
print(len('\t'))
print(len('\n'))
print(len(' '))
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