#/usr/bin/env python3

import json
import turtle
import urllib.request
import time
from math import log as _log, exp as _exp, pi as _pi, e as _e, ceil as _ceil

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
str_response = response.read().decode('utf-8')
result = json.loads(str_response)

print('People in Space: ', result['number'])
people = result['people']
for p in people:
  print(p['name'] + ' in ' + p['craft'])

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
str_response = response.read().decode('utf-8')
result = json.loads(str_response)

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
#screen.setup(360,180)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('iss2.gif')
iss = turtle.Turtle()
iss.shape('iss2.gif')
iss.setheading(90)

iss.penup()
iss.goto(float(lon), float(lat))

#Space Center, Houston
lat = 42.7654
lon = -71.4676

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
str_response = response.read().decode('utf-8')
result = json.loads(str_response)
print(result)

#print over
over = result['response'][1]['risetime']

style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)


