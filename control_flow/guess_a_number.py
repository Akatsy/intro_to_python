answer = int(input('Please input the number you want guessed: '))   #the number you want guessed
while True:
    guess = int(input('Please input your guess: '))   # the player's guess
    if answer > guess:
        print("Try a higher value")
    elif answer < guess:
        print("Try a lower value")
    elif answer == guess:
        print("Correct! That's the number!!")
        break