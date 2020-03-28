tab = '    '
print("If you declare a variable tab and assign to it one tab from the keyboard then len(tab) returns",len(tab))
print('#'*79)

tab_2 = '       '
print("If you declare a variable tab_2 and assign to it two tabs from the keyboard then len(tab_2) returns",len(tab_2))
print('#'*79)

tab_3 = '           '
print("If you declare a variable tab_3 and assign to it three tabs from the keyboard then len(tab_3) returns",len(tab_3))
print('#'*79)

newline = '''
'''
print("If you declare a variable newline and assign to it a multiline string like below\nnewline = '''\n'''\n then len(newline) will return ",len(newline))
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

# join() method
list = ['a', 'b', 'c', 'd']
joined = ''.join(list)
print(joined)
# print(joined.split('')) - you cannot use an empty seperator for the split method