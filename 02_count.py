# Imports
from time import sleep

from utils.leds import amber, green, onboardLED, red

counter = 1  # Set the counter to 1


# assign LEDs to binary digits LSB to MSB
led_bits = [red, amber, green, onboardLED]

while True:  # Keep on counting forever

    # count from 0 to 15 (2^4 values including 0, using 4 LEDs)
    for num in range(16):
        # convert to binary string but remove '0b' from the beginning
        binary = bin(num)[2:]
        # pad the left of the binary value with zeros
        binary = "%04d" % int(binary)
        # print the number and it's 4 digit binary equivalent
        print(f"{num} = binary {binary}")

        # loop over the 4 LED bits
        for bit, led_bit in enumerate(led_bits):
            # set the LED according to its equivalent position in the binary string
            led_bits[bit].value(int(binary[bit]))

        sleep(0.5)
