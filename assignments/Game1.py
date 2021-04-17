# Rock, Paper, Scissor

import random 

print("Let's Play Rock, Paper, Scissors")

# Computer's choice
computer_choice = random.choice(["scissors", "rock", "paper"])

# User's choice

user_choice = input("Do you want - rock, paper, or scissors? \n")
if computer_choice == user_choice:
    print("IT'S A TIE!")
elif user_choice == "rock" and computer_choice ==  "scissors":
    print("YOU WIN :D")
elif user_choice == "scissors" and computer_choice == "paper":
    print("YOU WIN :D")
elif user_choice == "paper" and computer_choice == "rock":
    print("YOU WIN :D")
else:
    print("YOU LOSE!!! :(, COMPUTER WINS :D")
    #     playerExit = input("Do you want to play again? y/n ")
    #     if playerExit == 'n':
    #         print("Hope you had fun, Bye!!")
    #         break
    #     else:
    #         print("Let's play again")
    #         continue
    # break
    
