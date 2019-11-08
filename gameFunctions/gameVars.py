#Import random package
from random import randint

# "basket" of choices
choices = ["rock", "paper", "scissors"]

# adding lvies, when one or the other gets to 0, win / lose
player_lives = 1
computer_lives = 1

total_lives = 1

# let the computer ai make a choice
computer = choices[randint(0,2)]

#set up a game loop here so we dont have to keep restarting it
player = False
