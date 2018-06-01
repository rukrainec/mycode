#!/usr/bin/env python3
#28 May 2018, Capstone exercise no. 1, 'Inventory Tracker'

####GOALS####
#Create a program that assumes inventory.txt will be local to where it was launched
#Each line in inventory.txt contains a real world thins and the location of the thing (Dictionary)
#Create 2 functions callable by the user from a repeating menu (while __ != 'q' loop)
#create a new entry
#search inventory for an entry, remove item if prompted by user

#How I intend this to work:
#Open dictionary from file, edit in program (NOT edit file directly)
#append changes, display updated inventory when user enters 'q'

import json #thing from API lab that read dictionary from remote file
InvDict = 'inventory.txt' #make calling the file easier in rest of script
newDict = {} #blank dictionary for adding new things to parent dictionary

#declare our functions
def new_item(name, box):  #function to add new item to inventory
    with open(InvDict) as working:
	    newDict = json.loads(working.read())
    newDict[name] = box
    with open(InvDict, 'w') as working:
        working.write(json.dumps(newDict))
    print(name + 'successfully added to inventory.')

def search_item(IName): #function to search for an item (key) and return the location (value)
    with open(InvDict) as working:
	    newDict = json.loads(working.read())
    try:
        print('The item you were looking for is in ' + newDict.get(IName) + '.')
    except:
        print('Item not found!')
    else:
        udel = input('Enter D to delete this item from the inventory \n Or hit \'Enter\'')
        if udel.upper() == 'D':
            newDict.pop(IName)
            with open(InvDict, 'w') as working:
                working.write(json.dumps(newDict))
            print('Item deleted')
        else:
            print('')

#functions are declared, blank variables set up, now make the program

print('Welcome to the inventory reader program.  This tool will tell you where to find things that you have packed into boxes for your move.')
while True: #infinite loop to cycle through until user hits 'q'
    action = input('What can I help you with? \n \'q\' to quit \n \'s\' to search \n \'a\' to add \n')
    if action.lower() == 'q':
        print('Thank you, I hope this was helpful')
        break
    elif action.lower() == 's':
        IName = input('What item do you need to find? \n')
        search_item(IName)
    elif action.lower() == 'a':
        name = input('What item are you adding? \n')
        box = input('What box did you put it in? \n')
        new_item(name, box)
    else:
        print('Invalid selection.  Please try again.')
print('Thank you for using this tool today.  The most up to date version of the inventory is:')
with open(InvDict) as working:
    newDict = json.loads(working.read())
    for item in newDict:
        print(item, newDict[item])
