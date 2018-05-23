#!/usr/bin/env python3
# 22 May 2018, Lab 16 'using while, if, elif, else'

round = 0 # starting out with a counter set at 0

while(True): # start the loop
    round = round +1 #increment counter
    print('Finish the movie title, "Monty Python\'s The Life of ______"') # prompt user for answer
    answer = input()
    if answer.lower() == 'brian': # if they get it right
        print('Correct!')
        break
    elif round == 3: # if they run the counter out
        print('Sorry, the answer was Brian.')
        break
# customization request: accept secret answer 'shrubbery'
    elif answer.lower() == 'shrubbery':
        print('You gave the super secret answer!')
        break
    else:
        print('Sorry! Try again!') # send a wrong answer back to the beginning
