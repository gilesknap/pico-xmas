# Imports
import random
import time

from machine import ADC, Pin
from neopixel import NeoPixel

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(26))

# Define the LED pin number (2) and number of LEDs (1)
GRBled = NeoPixel(Pin(28), 1)

# Create a flash speed variable
flash = 0

while True:
    # Read the potentiometer value
    flash = potentiometer.read_u16() / 65000

    # Generate random GRB values
    g = random.randint(0, 255)
    r = random.randint(0, 255)
    b = random.randint(0, 255)

    # Light the LED with the random GRB values
    GRBled.fill((g, r, b))
    GRBled.write()

    # Delay based on slider position
    time.sleep(flash)
