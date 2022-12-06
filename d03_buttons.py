# Imports

import time

from hardware.advent import amber, button1, button2, button3, green, onboardLED, red

print("Press a button to turn on an LED")

while True:  # Loop forever

    time.sleep(0.2)  # Short Delay

    # green LED tracks button 1, amber 2 and red 3
    green.value(button1.value())
    amber.value(button2.value())
    red.value(button3.value())

    # onboard is on when no buttons are pressed
    onboardLED.value(not (button1.value() or button2.value() or button3.value()))
