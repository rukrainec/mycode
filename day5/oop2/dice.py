#!/usr/bin/env python3
#25 May 2018, Lab 35

from cheatdice import *           #importing the classes and functions from file in working directory
swapper = Cheat_Swapper()         #object of class swapper
loaded_dice = Cheat_Loaded_Dice() #object of class loaded
swapper_score = 0                 #starting scores
loaded_dice_score = 0             
number_of_games = 1000000         #target # of iterations to hit
game_number = 0                   #current iteration
print("Simulation running")
print("==================")
while game_number < number_of_games: #while loop to iterate games until target hit
    swapper.roll()                   # next few lines go through functions that roll and add cheats
    loaded_dice.roll()
    swapper.cheat()
    loaded_dice.cheat()
   #Remove # before print statements to see simulation running
   #Simulation takes approximately one hour to run with print
   #statements or ten seconds with print statements
   #commented out

 #print("Cheater 1 rolled" + str(swapper.get_dice()))
 #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
    if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):    #if/elif/else determines winner
 #    print("Draw!")
        pass
    elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
 #    print("Dice swapper wins!")
        swapper_score+= 1

    else:
 #print("Loaded dice wins!")
        loaded_dice_score += 1
    game_number += 1                                              #increments game iteration and restarts 
print("Simulation complete")                                      #loop
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))                       #lines 40-47 provide final scorecard
print("Loaded dice won: " + str(loaded_dice_score))
if swapper_score == loaded_dice_score:
    print("Game was drawn")
elif swapper_score > loaded_dice_score:
    print("Swapper won most games")
else:
    print("Loaded dice won most games")
