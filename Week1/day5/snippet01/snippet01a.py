#!/usr/bin/env python3
#25 May 2018, lab 32 'snippet.split.join'

###goals###
#open a text file from wd
#split file into list
#use print(\n.join(list))
#use .join to place tabs between items

source = open('source.txt', 'r') #open the text file
sauce = source.readline() #put text file into buffer
slist = sauce.split() #make a list
print('\n'.join(slist)) #print the joined list (joined with new lines)

