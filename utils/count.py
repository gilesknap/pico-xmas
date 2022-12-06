from hardware.advent import amber, green, onboardLED, red


class BinCounter:
    """
    A class to implement a binary counter and display the value using 4 LEDs.

    :member forwards: True for forwards, False for backwards
    :member value: The current value of the counter
    :member silent: True to suppress printing the value
    """

    # assign LEDs to binary digits LSB to MSB
    led_bits = [green, amber, red, onboardLED]

    def __init__(self, forwards=True, silent=True):
        """Initialise the counter with the given pause between steps and direction."""
        self.forwards = forwards
        self.silent = silent
        self.value = 0

    @classmethod
    def to_binary(cls, num: int) -> str:
        """convert a number to a 4 digit binary string"""

        # convert to binary string but remove '0b' from the beginning
        binary = bin(num)[2:]
        # pad the left of the binary value with zeros
        return "%04d" % int(binary)

    @classmethod
    def show_binary_leds(cls, binary: str):
        """display the binary value on the LEDs"""

        # loop over the 4 LED bits
        for bit, led_bit in enumerate(cls.led_bits):
            # set the LED according to its equivalent position in the binary string
            cls.led_bits[bit].value(int(binary[bit]))

    def count_led(self):
        """count one in the current direction and display the value on the LEDs"""

        # move to the next value
        self.value += 1 if self.forwards else -1
        # wrap around if we go over 15 or under 0
        self.value %= 16

        binary = self.to_binary(self.value)

        if not self.silent:
            print(f"{self.value} = binary {binary}")

        self.show_binary_leds(binary)
