#imports random package
from random import randint

#creates a basket or choices to choose from
choices=["rock", "paper", "scissors"]

# let the computer ai make a choice
computer=choices[randint(0,2)]

#set up a game loop here so we dont have to keep restarting it
player= False

#game loop
while player is False:
    player=input ("choose rock, paper or scissors: \n")

    #Checks to confirm it works
    print("computer:", computer, "player", player)

    #always check a breaking condition first
    if player == computer:
    #we have a tie, no point in going any further
        print("Tie, no one wins! Try again")
    elif player == "quit":
    #you quit, lets player exit game
        print("You choose to quit, quitter.")
        exit()

    #Rock against (Paper or Scissors)
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player, "\n")
        else:
            print("You won!", player, "smashes", computer, "\n")

    #Paper against (Scissors or Rocks)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cuts", player, "\n")
        else:
            print("You won!", player, "covers", computer, "\n")

    #Scissors against (Rock or paper)
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "smashes", player, "\n")
        else:
            print("You won!", player, "cuts", computer, "\n")

    player = False
    computer = choices[randint(0,2)]
