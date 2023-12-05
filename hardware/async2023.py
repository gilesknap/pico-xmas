"""
ASYNC Configuration for interfacing with the Hardware supplied
in the PiHut Advent Calendar 2023
"""
from asyn.button import Button
from utils.led import Led

# day 1 LED
onboard_led = Led(25)
# day 2 LED
red_led = Led(14)

# day 3 buttons
red_button = Button(pin_num=2)
green_button = Button(pin_num=3)
