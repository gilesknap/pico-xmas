# Imports
import time

from machine import Pin

# Set up input pins
red_button = Pin(2, Pin.IN, Pin.PULL_DOWN)
green_button = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up output pins
red_led = Pin(14, Pin.OUT)

while True:

    time.sleep(0.2)

    if red_button.value() == 1:
        print("Light OFF")
        red_led.value(0) # LED pin LOW

    if green_button.value() == 1:
        print("Light ON")
        red_led.value(1) # LED pin HIGH