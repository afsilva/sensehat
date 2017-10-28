#!/usr/bin/python
from sense_hat import SenseHat
import time

sense = SenseHat()
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
blue = (0,255,255)
sense.show_message("left: help // middle: quit")

while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed' and event.direction == 'right':
            pressure = sense.get_pressure()
            pressure = round(pressure, 1)
            sense.show_message("%smbr" % str(pressure), text_colour=blue)
        if event.action == 'pressed' and event.direction == 'down':
            humidity = sense.get_humidity()
            humidity = round(humidity, 1)
            sense.show_message("%s%%" % str(humidity), text_colour=white)
        if event.action == 'pressed' and event.direction == 'left':
            sense.show_message("up: temp, down: humidity, middle: quit", text_colour=yellow)
            sense.clear(black)
        if event.action == 'pressed' and event.direction == 'middle':
            sense.show_message("bye", text_colour=black, back_colour=white)
            sense.clear(black)
            quit() 
        if event.action == 'pressed' and event.direction == 'up':
            temp = ((sense.get_temperature() / 5 ) * 9) + 32
            if temp < 50:
                color = blue
            elif temp >= 50 and temp <= 80: 
                color = green
            else:
                color = red
            sense.show_message("%sF" % str(int(temp)), text_colour=color)
