#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
red = (255, 0, 0)
blue = (0, 0, 255)
sense.show_message("Hello boys! Have a good day!", text_colour=red,back_colour=blue)
