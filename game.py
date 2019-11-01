#imports random package
from random import randint

#creates a basket or choices to choose from
choices=["rock", "paper", "scissors"]

#Lives
player_lives = 5
computer_lives = 5

# let the computer ai make a choice
computer=choices[randint(0,2)]

#set up a game loop here so we dont have to keep restarting it
player= False

#game loop
while player is False:
    print('=====================================================')
    print('Computer Lives:', computer_lives, "/5")
    print('Player Lives:', player_lives, "/5")
    print('=====================================================')
    player=input ("choose rock, paper or scissors: \n")

    #Checks to confirm it works
    #print("computer:", computer, "player", player)

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
            player_lives -= 1
        else:
            print("You won!", player, "smashes", computer, "\n")
            computer_lives -= 1

    #Paper against (Scissors or Rocks)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cuts", player, "\n")
            player_lives -= 1
        else:
            print("You won!", player, "covers", computer, "\n")
            computer_lives -= 1

    #Scissors against (Rock or paper)
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "smashes", player, "\n")
            player_lives -= 1
        else:
            print("You won!", player, "cuts", computer, "\n")
            computer_lives -= 1

    if player_lives == 0:
        print("You Lost! Loser. Would you like to play again?")
        choice = input('Y / N?')

        if choice == "Y" or choice == "y":
            player_lives = 5
            computer_lives = 5
            player = False
            computer = choices[randint(0,2)]

        elif choice == "N" or choice == "n":
            print("You chose to quit.  Better luck next time")
            exit()
        else:
            print("Make a valid choice Yes or No")

    elif computer_lives == 0:
        print("You Won! Loser. Would you like to play again?")
        choice = input('Y / N?')

        if choice == "Y" or choice == "y":
            #resets the game
            player_lives = 5
            computer_lives = 5
            player = False
            computer = choices[randint(0,2)]

        elif choice == "N" or choice == "n":
            print("You chose to quit.  Better luck next time")
            exit()
        else:
            print("Make a valid choice Yes or No")
            #choice = input('Y / N?')

    else:
        player = False
        computer = choices[randint(0,2)]
