answer = 56   #the number you want guessed
guess = 34    # the player's guess

if answer > guess:
    print("Try a higher value")
elif answer < guess:
    print("Try a lower value")
elif answer == guess:
    print("Correct! That's the number!!")