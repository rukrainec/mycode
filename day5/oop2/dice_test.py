#!/usr/bin/env python3
#25 May 2018, Lab 34b

from cheatdice import Player #non-cheating player class with standard dice rolling
from cheatdice import Cheat_Swapper #cheater that always gets a 6 for 3rd roll
from cheatdice import Cheat_Loaded_Dice #cheater that uses loaded dice (loaded in this case adds 1 to every roll less than 6)

cheater1 = Cheat_Swapper() #cheater1 always gets a 6 via cheat_swap func
cheater2 = Cheat_Loaded_Dice() #cheater2 gets +1 for every roll via cheat_load func

#standard rolls that feed the cheating functions
cheater1.roll()
cheater2.roll()

#cheating functions executed, same verbiage 'cheat()' but maps to different classes/cheats
cheater1.cheat()
cheater2.cheat()

#display values of rolls
print("Cheater 1 rolled" + str(cheater1.get_dice()))
print("Cheater 2 rolled" + str(cheater2.get_dice()))

#if/elif/else operator to determine winner
if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
  print("Draw!")

elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
  print("Cheater 1 wins!")

else:
  print("Cheater 2 wins!")
