# Imports
import time
from _thread import start_new_thread

from utils.leds import amber, green, onboardLED, red


class BinCounter:
    """
    A class to implement a binary counter using 4 LEDs. It provides a thread
    to run the counter in the background. Speed and direction can be changed
    while the counter is running via public member variables.

    :member pause: The time to pause between steps (sec)
    :member forwards: True for forwards, False for backwards
    :member running: True if the counter is running, False if not
    :member value: The current value of the counter
    """

    # assign LEDs to binary digits LSB to MSB
    led_bits = [green, amber, red, onboardLED]

    def __init__(self, pause=0.2, forwards=True, silent=True):
        """
        Initialise the counter with the given pause between steps and direction.
        """
        self.pause = pause
        self.forwards = forwards
        self.silent = silent
        self.value = 0
        self._running = False

    def count_led(self):
        """
        worker function to run the counter in the background
        """
        while self._running:
            # convert to binary string but remove '0b' from the beginning
            binary = bin(self.value)[2:]
            # pad the left of the binary value with zeros
            binary = "%04d" % int(binary)

            if not self.silent:
                print(f"{self.value} = binary {binary}")

            # loop over the 4 LED bits
            for bit, led_bit in enumerate(self.led_bits):
                # set the LED according to its equivalent position in the binary string
                self.led_bits[bit].value(int(binary[bit]))

            # move to the next value
            self.value += 1 if self.forwards else -1
            # wrap around if we go over 15 or under 0
            self.value %= 16

            time.sleep(self.pause)

    def start(self):
        # start the worker loop running count_led()
        print("Starting counter")
        self._running = True
        start_new_thread(self.count_led, ())

    def stop(self):
        # cause the worker loop to exit
        print("Stopping counter")
        self._running = False
