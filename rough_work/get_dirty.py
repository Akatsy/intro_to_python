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