"""
ASYNC Configuration for interfacing with the Hardware supplied
in the PiHut Advent Calendar 2023
"""
from asyn.button import Button
from asyn.led import Led

# day 1 LED
onboard_led = Led(25)

# day 2 LED
red_led = Led(14)

# day 3 segmented display
seg1_led = Led(13)
seg2_led = Led(12)
seg3_led = Led(11)
seg4_led = Led(10)
seg5_led = Led(9)
segments = [seg1_led, seg2_led, seg3_led, seg4_led, seg5_led]


# day 3 buttons
def red_button(callback=None):
    return Button(pin_num=2, name="Red", handler=callback)


def green_button(callback=None):
    return Button(pin_num=3, name="Green", handler=callback)
