from random import randint
from gameFunctions import gameVars
#importing the random number pachage again for this file


#game win and loose run.
def winorlose(status):
    print("Called win or lose", status, "\n")
    print("You", status, "! Would you like to play again")
    choice = input('Y / N? ')

#yes choice at the end of the game
    if choice == "Y" or choice == "y":
        #resets the game
        gameVars.player_lives = 1
        gameVars.computer_lives = 1
        gameVars.player = False
        gameVars.computer = gameVars.choices[randint(0,2)]

#no choice at the end of the game
    elif choice == "N" or choice == "n":
        print("You chose to quit.  Better luck next time")
        exit()
    else:
        print("Make a valid choice Yes or No")
        #recursion => calling a function from inside itself
        winorlose(status)
        #choice = input('Y / N?')
