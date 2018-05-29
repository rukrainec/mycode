#!/usr/bin/env python3
#29 May 2018, lab 41 'More APIs... Vast'

## Customization requests:
#1:redo to call 1 or more functions
#2:prompt user for their lat/long

#import the things
import urllib.request
import json
import turtle
import time

def nextpass(yellowlat, yellowlon):
    passiss = 'http://api.open-notify.org/iss-pass.json'
    passiss = passiss + '?lat=' + str(yellowlat) + '&lon=' + str(yellowlon)
    response = urllib.request.urlopen(passiss)
    result1 = response.read()
    result = json.loads(result1.decode('utf-8'))
    over = result['response'][0]['risetime']
    style = ('Arial', 6, 'bold')
    mylocation.write(time.ctime(over), font=style)

#declare base variables, urls, etc
eoss = 'http://api.open-notify.org/iss-now.json'
trackiss = urllib.request.urlopen(eoss)
ztrack = trackiss.read()
result = json.loads(ztrack.decode('utf-8'))
location = result['iss_position']
lat = location['latitude']
lon = location['longitude']

#get lat/long from user
yellowlat = float(input('What is your lattitude in degrees?'))
yellowlon = float(input('What is your longitude in degrees?'))
mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color('yellow')
mylocation.goto(yellowlon, yellowlat)
mylocation.dot(5)

#add turtle stuff to format map/screen
screen = turtle.Screen() #create object
screen.setup(720, 260) #set resolution
screen.bgpic('iss_map.gif') #select image for object
screen.setworldcoordinates(-180,-90,180,90)

#format sprite to represent iss on map
screen.register_shape('spriteiss.gif')
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

#set spriteiss location on map to lat/lon from eoss (line 7)
lon = round(float(lon))  #These 2 lines approximate iss location
lat = round(float(lat))  #because rounding them makes them easier
iss.penup()
iss.goto(lon, lat)


turtle.mainloop()

nextpass(yellowlat, yellowlon)
