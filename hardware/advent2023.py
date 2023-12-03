"""
Configuration for interfacing with the Hardware supplied
in the PiHut Advent Calendar 2023
"""
from machine import Pin

from utils.led import Led

# day 1 LED
onboard_led = Led(25)
# day 2 LED
red_led = Led(14)

# day 3 buttons
red_button = Pin(2, Pin.IN, Pin.PULL_DOWN)
green_button = Pin(3, Pin.IN, Pin.PULL_DOWN)