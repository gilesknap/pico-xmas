# Imports
import time

from utils.leds import amber, green, onboardLED, red

counter = 1  # Set the counter to 1


# assign LEDs to binary digits LSB to MSB
led_bits = [green, amber, red, onboardLED]


def count_led(pause=0.2, iterations=1, silent=False):
    start_time = time.time()  # Get the current time

    for num in range(iterations):  # Loop 16 times

        # count from 0 to 15 (2^4 values including 0, using 4 LEDs)
        for num in range(16):
            # convert to binary string but remove '0b' from the beginning
            binary = bin(num)[2:]
            # pad the left of the binary value with zeros
            binary = "%04d" % int(binary)
            # print the number and it's 4 digit binary equivalent
            if not silent:
                print(f"{num} = binary {binary}")

            # loop over the 4 LED bits
            for bit, led_bit in enumerate(led_bits):
                # set the LED according to its equivalent position in the binary string
                led_bits[bit].value(int(binary[bit]))

            time.sleep(pause)

    interval = time.time() - start_time  # Get the time since we started
    print(f"Counted from 0 to 15 {iterations} times in {interval} seconds")


count_led()
