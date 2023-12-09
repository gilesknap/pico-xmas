# Imports
import time

from machine import Pin
from neopixel import NeoPixel

# Define the RGB LEDs
GRBled1 = NeoPixel(Pin(28), 1)
GRBled2 = NeoPixel(Pin(27), 1)

# set up some tuples for the colours to make the code more readable
red = (1, 0, 0)
green = (0, 1, 0)
blue = (0, 0, 1)
colours = [red, green, blue]

# tuples for making ascending and descending ranges for 0-255 with no overlaps
ascend = (1, 255, 1)
descend = (254, 0, -1)


def set_leds(led1, led2, colour1, colour2, factor):
    """
    Set led1 to colour 1 with brightness factor
    set led2 to colour 2 with inverse brightness factor
    """
    inverse_factor = 255 - factor
    brightness = tuple(factor * colour1[i] for i in range(3))
    inverse_brightness = tuple(inverse_factor * colour2[i] for i in range(3))

    led1.fill(brightness)
    led2.fill(inverse_brightness)
    led1.write()
    led2.write()


# some initial value for state variables
num1 = 0
num2 = 0
direction = ascend

# main loop, ascends and descends the brightness of the two LEDs
# flipping over to the next colour when the brightness is at minimum
while True:
    for factor in range(*direction):
        set_leds(GRBled1, GRBled2, colours[num1], colours[num2], factor)
        time.sleep(0.005)

        # roll over the colour when the brightness is at minimum
        if factor == 1:
            num1 = (num1 + 1) % 3
        elif factor == 254:
            num2 = (num2 + 1) % 3

    # use the direction tuples to flip the direction
    direction = descend if direction == ascend else ascend
