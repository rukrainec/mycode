#!/usr/bin/env python3
#29 May 2018, lab 41 'More APIs... Vast'
import urllib.request
import json
import turtle
import time
## Trace the ISS - earth-orbital space station
eoss = 'http://api.open-notify.org/iss-now.json'

## Call the webserv
trackiss = urllib.request.urlopen(eoss)

## put into file object
ztrack = trackiss.read()

## json 2 python data structure
result = json.loads(ztrack.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(result)
input('\nISS data retrieved & converted. Press any key to continue')    

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude: ', lat)
print('Longitude: ', lon)

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
#turtle.mainloop() goes at the end of all the turtles

# add my location on map
yellowlat = 47.6
yellowlon = -122.3
mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color('yellow')
mylocation.goto(yellowlon, yellowlat)
mylocation.dot(5)


#for some reason yellowdot shows up off Baja

passiss = 'http://api.open-notify.org/iss-pass.json'
passiss = passiss + '?lat=' + str(yellowlat) + '&lon=' + str(yellowlon)
response = urllib.request.urlopen(passiss)
result1 = response.read()
result = json.loads(result1.decode('utf-8'))
over = result['response'][0]['risetime']

style = ('Arial', 6, 'bold')
mylocation.write(time.ctime(over), font=style)
turtle.mainloop()
