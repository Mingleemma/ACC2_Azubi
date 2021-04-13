# Lab 6: Loops

# Exercise 1: The while loop

import random

print("Welcome to Guess The Number!")
print("The rules are simple. I think of a number and you try to guess it.")

# Think of a number between 1 and 10.
number = random.randint(1,10)
isGuessRight = False

# If the user has not guessed the right answer, enter the loop.
while isGuessRight != True:
    # Ask the user for a guess.
    guess = input("Guess a number between 1 and 10: ")
    # Is the gues the right number?
    if int(guess) == number:
        # If the right guess, tell the uesr it was the right guess
        # and continue the loop.
        print("You guessed {}. That is right! You win!".format(guess))
        isGuessRight = True
    else:
        # if the wrong guess, tell the user it was the wrong guess and
        # continue the loop.
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))
        
