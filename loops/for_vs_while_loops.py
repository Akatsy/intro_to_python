print('#' * 99)
#PRACTICE
# Question: What type of loop should we use?
# You need to write a loop that takes the numbers in a given list named num_list:
# num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

# Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
import time
print("seconds since epoch: {}".format(time.time()))
print("local time: {}".format(time.ctime()))
print('#' * 99)
t1 = time.time()
odd_num_list = []
for num in num_list:
    if num % 2 != 0:
        if len(odd_num_list) < 5:
            odd_num_list.append(num)
print(odd_num_list)
print(sum(odd_num_list))
t2 = time.time()
print(t1, t2)
print("It took {} seconds to execute".format(t2-t1))

print('#' * 99)
# add break statement so we do not loop over the whole list
t3 = time.time()
odd_num_list = []
for num in num_list:
    if num % 2 != 0:
        if len(odd_num_list) < 5:
            odd_num_list.append(num)
        else:
            break
# print(odd_num_list)
print(sum(odd_num_list))
t4 = time.time()
print(t3, t4)
print("It took {} seconds to execute".format(t4-t3))
print('#' * 99)
print("Is the execution time of the for loop with break statement and without less? {}".format((t4-t3)<(t2-t1)))


print('#' * 99)

# solution using while loop
t5 = time.time()
odd_num_sum = 0
odd_num_count = 0
index = 0
len_num_list = len(num_list)
while index < len_num_list and odd_num_count < 5:
    if num_list[index] % 2 != 0:
        odd_num_count += 1
        odd_num_sum += num_list[index]
    index += 1
print(odd_num_sum)
t6 = time.time()
print(t5, t6)
print("It took {} seconds to execute".format(t6-t5))
print('#' * 99)
print("Is the execution time of the for loop without break statement less than that of the while loop? {}".format((t2-t1)<(t6-t5)))
print("Is the execution time of the for loop with break statement less than that of the while loop? {}".format((t4-t3)<(t6-t5)))