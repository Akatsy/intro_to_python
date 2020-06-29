print(r'''
Flow control statements often start with a part called the condition and are
always followed by a block of code called the clause

Conditions are expressions that always evaluate to True or False

The clauses are blocks of code which is just Python lines of code grouped together
There are 3 rules for blocks:
1. Blocks begin when indentation increases
2. Blocks can contain other blocks
3. Blocks end when the indentation decreases to zero or to a containing's block
indentation
''')
print('#' * 99)

phone_balance = 10
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance)
print(bank_balance)

#Second Example - try changing the value of number

number = int(input('Enter a number: '))
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

#Third Example - try to change the value of age
age = int(input('Enter age of passenger: '))

# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)

print('#' * 99)