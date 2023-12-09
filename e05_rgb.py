# Imports
import time

from machine import Pin
from neopixel import NeoPixel

# Define the RGB LEDs
GRBled1 = NeoPixel(Pin(28), 1)
GRBled2 = NeoPixel(Pin(27), 1)

# set up some tuples for the colours
white = 240, 140, 255  # White-ish!
red = 0, 255, 0
green = 255, 0, 0
blue = 0, 0, 255
yellow = 255, 175, 150
orange = 238, 223, 105
pink = 150, 150, 200
purple = 40, 100, 255
ice_blue = 150, 25, 200
unicorn = 175, 150, 255
bogey = 215, 100, 0
colours = [
    white,
    red,
    green,
    blue,
    yellow,
    orange,
    pink,
    purple,
    ice_blue,
    unicorn,
    bogey,
]

# tuples for making ascending and descending ranges for 0-255 with no overlaps
ascend = (0, 255, 1)
descend = (255, 0, -1)


def set_leds(led1, led2, colour1, colour2, factor):
    """
    Set led1 to colour 1 with brightness factor
    set led2 to colour 2 with inverse brightness factor
    """
    inverse_factor = 255 - factor
    brightness = tuple(factor / 255 * colour1[i] for i in range(3))
    inverse_brightness = tuple(inverse_factor / 255 * colour2[i] for i in range(3))

    # we did some floating point maths, so we need to convert back to integers
    b1 = tuple(map(int, brightness))
    b2 = tuple(map(int, inverse_brightness))
    # set the LEDs to the calculated brightness
    led1.fill(b1)
    led2.fill(b2)
    led1.write()
    led2.write()


# some initial value for state variables
num1 = 0
num2 = 2
direction = ascend

# main loop, ascends and descends the brightness of the two LEDs
# flipping over to the next colour when the brightness is at minimum
while True:
    for factor in range(*direction):
        set_leds(GRBled1, GRBled2, colours[num1], colours[num2], factor)
        time.sleep(0.005)

        # roll over the colour when the brightness is at minimum
        if factor == 0:
            num1 = (num1 + 1) % len(colours)
        elif factor == 255:
            num2 = (num2 + 1) % len(colours)

    # use the direction tuples to flip the direction
    direction = descend if direction == ascend else ascend
