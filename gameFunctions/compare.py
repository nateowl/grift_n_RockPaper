from gameFunctions import gameVars

def gameFunction(player):
    #always check a breaking condition first
    if player == gameVars.computer:
    #we have a tie, no point in going any further
        print(gameVars.line)
        print("Tie, no one wins! Try again")
    elif player == "quit":
    #you quit, lets player exit game
        print(gameVars.line)
        print("You choose to quit, quitter.")
        print(gameVars.line)
        exit()

    #Rock against (Paper or Scissors)
    elif player == "rock":
        if gameVars.computer == "paper":
            print(gameVars.line)
            print("You lose!", gameVars.computer, "covers", player)
            gameVars.player_lives -= 1
        else:
            print(gameVars.line)
            print("You won!", player, "smashes", gameVars.computer)
            gameVars.computer_lives -= 1

    #Paper against (Scissors or Rocks)
    elif player == "paper":
        if gameVars.computer == "scissors":
            print(gameVars.line)
            print("You lose!", gameVars.computer, "cuts", player)
            gameVars.player_lives -= 1
        else:
            print(gameVars.line)
            print("You won!", player, "covers", gameVars.computer)
            gameVars.computer_lives -= 1

    #Scissors against (Rock or paper)
    elif player == "scissors":
        if gameVars.computer == "rock":
            print(gameVars.line)
            print("You lose!", gameVars.computer, "smashes", player)
            gameVars.player_lives -= 1
        else:
            print(gameVars.line)
            print("You won!", player, "cuts", gameVars.computer)
            gameVars.computer_lives -= 1
