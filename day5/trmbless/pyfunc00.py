#!/usr/bin/env python3
#25 May 2018, Lab 31 'defining functions'

from blessings import Terminal #blessings is some thing made by some dude named Kevin that makes it a lot easier for us to manipulate (among other things) the terminal
import os # more imported tools/libraries(?)
import sys

t = Terminal() #set variable to save typing time
print(t.clear()) #terminal.clear() is like entering $clear

def close(event): #I'm not sure what this does
    master.withdraw()
    sys.exit()

def yellow_wp(p): #function with-parameters, prints text in color
    print(t.bold_black_on_yellow(p))

def trx(p): # function that right-aligns string p in terminal window
    x = t.width - len(p)
    return int(x)

def top_right(p): # function to execute yellow_wp(p) function in top right
    with t.location(trx(p), 0):
        yellow_wp(p)

def prompt_location(): # function that bottom-right aligns text in terminal window
    return t.location(0,t.height-2)

def response_location(p): #sets location of user input IRT prompt_loc; 2 from bottom, 1 to the right of end of (p)
    return t.location(len(p) +1,t.height-2)

def prompt(p): # function that establishes process for user to input data in bottom left
    with prompt_location():
        print(t.reverse(p))
    with response_location(p):
        orders = input()
    return orders

#top_right('I want this in the top right!')

orders = "" # set variable null to begin with
while orders.lower() != 'q': #while loop to allow program to continue until user quits
    orders = prompt('Your orders') #runs def prompt(p) to get value of orders
    orders
    top_right(orders) #puts order you entered in top right
    if orders[:3]=='mtr': #very specific if to run 'mtr 8.8.8.8' via os and sys and display results 3 rows down, left aligned
        with t.location(0,3):
            os.system(orders)

yellow_wp('Thanks for all the fish!') #closeout message via def yellow_wp
