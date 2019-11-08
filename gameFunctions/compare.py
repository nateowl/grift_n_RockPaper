from gameFunctions import gameVars

def gameFunction(status):
    #always check a breaking condition first
    if status == gameVars.computer:
    #we have a tie, no point in going any further
        print("Tie, no one wins! Try again")
    elif status == "quit":
    #you quit, lets player exit game
        print("You choose to quit, quitter.")
        exit()

    #Rock against (Paper or Scissors)
    elif status == "rock":
        if gameVars.computer == "paper":
            print("You lose!", gameVars.computer, "covers", status, "\n")
            gameVars.player_lives -= 1
        else:
            print("You won!", status, "smashes", gameVars.computer, "\n")
            gameVars.computer_lives -= 1

    #Paper against (Scissors or Rocks)
    elif status == "paper":
        if gameVars.computer == "scissors":
            print("You lose!", gameVars.computer, "cuts", status, "\n")
            gameVars.player_lives -= 1
        else:
            print("You won!", status, "covers", gameVars.computer, "\n")
            gameVars.computer_lives -= 1

    #Scissors against (Rock or paper)
    elif status == "scissors":
        if gameVars.computer == "rock":
            print("You lose!", gameVars.computer, "smashes", status, "\n")
            gameVars.player_lives -= 1
        else:
            print("You won!", status, "cuts", gameVars.computer, "\n")
            gameVars.computer_lives -= 1
