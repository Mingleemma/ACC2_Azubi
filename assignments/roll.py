# Dice Roll Guess Game
print("LET'S PLAY A GUESS GAME")

import random

roll = random.randint(1,6)
guess = int(input("Guess what the computer rolled: \n"))

if guess ==roll:
    print("Correct! It rolled a " + str(roll) + ".")
else:
    print("Wrong! It rolled a " + str(roll) + ".")
    print("Try Again!!!")

