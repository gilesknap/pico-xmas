import asyncio
import re
import time

from machine import Pin

pin_regex = re.compile(r"GPIO(\d+)")


def pin_number(pin: Pin):
    """
    Crazily enough, its a bit hard to get the pin number from a Pin object
    But if you use repr() on the Pin object you get a string like this:
    - Pin(GPIO2, mode=IN, pull=PULL_DOWN)
    So we can use a regex to extract the pin number from that string.
    """
    if match := pin_regex.search(repr(pin)):
        return int(match.group(1))

    return -1


class Button:
    """
    A class to represent a button attached to a GPIO on the Pico.

    This is an async implementation that allows us to monitor multiple
    buttons at the same time.
    """

    irq = None
    callbacks = {}
    debug = False

    def __init__(
        self, pin_num: int, name: str, handler=None, debounce_ms: int = 30, debug=False
    ):
        # there is one interrupt handler for all buttons so we track the
        # Button instance to pin number relationship in a class variable
        Button.debug = debug
        self.pin = Pin(pin_num, Pin.IN, Pin.PULL_DOWN)
        self.num = pin_num
        if Button.irq is None:
            Button.irq = self.pin.irq(
                handler=Button._isr, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING
            )
        Button.callbacks[pin_num] = self._callback

        self.debounce_ms = debounce_ms
        self.last_press = time.ticks_ms()

        self.pressed = 0  # 0 = released, 1 = pressed
        self.handler = handler or self.print_state  # default handler prints state
        self.name = name

    @classmethod
    def _isr(cls, pin):
        """
        The interrupt handler that is called when any button is pressed.
        """
        num = pin_number(pin)
        if cls.debug:
            print(f"Button._isr num={num}, value={pin.value()} pin={pin}")
        if num in cls.callbacks:
            cls.callbacks[num]()

    def _callback(self):
        """
        The callback function that is called when the button is pressed.
        """
        print("Button._callback", self.pressed, self.num)
        # debounce the button
        now = time.ticks_ms()
        diff = now - self.last_press
        if diff > self.debounce_ms:
            self.last_press = now
            self.pressed = self.pin.value()

    async def wait_for_press(self):
        """
        async monitoring of button state
        """
        while not self.pressed:
            await asyncio.sleep(0.03)

    def print_state(self):
        """print the state of the button"""
        print(self)

    def __repr__(self):
        """return a string representation of the button"""
        return (
            f"{self.name} Button({self.pin}) is "
            + f"{'pressed' if self.pressed else 'released'}"
        )


if __name__ == "__main__":
    # test code
    async def main():
        print("Testing Button class with pins 2,3")
        button1 = Button(2, "Red", debug=True)

        await button1.wait_for_press()
        print(button1)

    asyncio.run(main())
