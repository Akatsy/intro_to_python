print("Input validation checks that values entered by the user in your program are formatted correctly")
print("This helps in avoiding bugs, making sure your programs do not crash later on due to invalid values for example if you ask a user for their age, you expect a number (digit value) - an integer to be precise which should not be negative ofcourse. If a user input does not adhere to the above rules, you should prompt them to re-enter the value again")

print('#' * 99)

print("Input validation also can help avoid security vulnerabilities")
print("For example say you were implementing a withdraw_from_account() function and the user had to input the amount they want to withdraw. You have to make sure that the user does not enter a negative amount because subtracting a negative amount from the account would end up actually adding.Therefore, the 'withdrawal' would end up adding money to the account instead of subtracting")

print('#' * 99)

# input validation example
while True:
    age = input("Enter your age:\n")
    try:
        age = int(age)
    except:
        print("Please input a number in digits")
        continue
    if age < 1:
        print("Age cannot be negative. Input a positive number")
        continue
    elif age > 150:
        print("You cannot be that old. Come on!!")
        continue
    else:
        break
print(f'Hey {age} years old human!')

print('#' * 99)