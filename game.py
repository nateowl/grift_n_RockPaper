#imports random package
from random import randint
from gameFunctions import winlose, gameVars, compare

#game loop
while gameVars.player is False:
    print('=====================================================')
    print('Computer Lives:', gameVars.computer_lives, "/", gameVars.total_lives)
    print('Player Lives:', gameVars.player_lives, "/", gameVars.total_lives)
    print('=====================================================')
    player=input ("choose rock, paper or scissors: \n")

    #Checks to confirm it works
    #print("computer:", computer, "player", player)
    compare.gameFunction(player)

    if gameVars.player_lives == 0:
        winlose.winorlose("lost")

    elif gameVars.computer_lives == 0:
        winlose.winorlose("won")

    else:
        player = False
        gameVars.computer = gameVars.choices[randint(0,2)]
