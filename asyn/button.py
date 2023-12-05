import asyncio
import re
import time

from machine import Pin

pin_regex = re.compile(r"GPIO(\d+)")


class Button:
    """
    A class to represent a button attached to a GPIO on the Pico.

    This is an async implementation that allows us to monitor multiple
    buttons at the same time.
    """

    debug = False

    def __init__(
        self, pin_num: int, name: str, handler=None, debounce_ms: int = 30, debug=False
    ):
        # there is one interrupt handler for all buttons so we track the
        # Button instance to pin number relationship in a class variable
        Button.debug = debug
        self.pin = Pin(pin_num, Pin.IN, Pin.PULL_DOWN)
        self.num = pin_num
        self.irq = self.pin.irq(
            handler=self._callback, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING
        )

        self.debounce_ms = debounce_ms
        self.last_state_change = time.ticks_ms()

        self.pressed = 0  # 0 = released, 1 = pressed
        self.handler = handler or self.print_state  # default handler prints state
        self.name = name

    def _callback(self, _):
        """
        The callback function that is called when the button is pressed.
        """
        value = self.pin.value()

        if Button.debug:
            print(
                f"_callback: {self.name} pressed={self.pressed}, "
                + f"value={value}, num={self.num}"
            )

        # only interested in transitions of button state
        if value != self.pressed:
            # debounce the button
            now = time.ticks_ms()
            diff = now - self.last_state_change
            if diff > self.debounce_ms:
                self.last_state_change = now
                self.pressed = value
                self.handler(self)
            else:
                if Button.debug:
                    print("{self.name} debounce")

    async def wait_for_press(self):
        """
        async monitoring of button state
        """
        while not self.pressed:
            await asyncio.sleep(0.05)

    async def wait_for_release(self):
        """
        async monitoring of button state
        """
        while self.pressed:
            await asyncio.sleep(0.05)

    @staticmethod
    def print_state(button):
        """print the state of the button"""
        print(button)

    def __repr__(self):
        """return a string representation of the button"""
        return f"{self.name} " + f"{'pressed' if self.pressed else 'released'}"


if __name__ == "__main__":
    # test code
    async def main():
        print("Testing Button class with pins 2,3")
        button1 = Button(2, "Red")
        button2 = Button(3, "Green", debug=True)

        print("Waiting for button 1 to be pressed")
        await button1.wait_for_press()
        await button1.wait_for_release()
        print("Waiting for button 2 to be pressed")
        await button2.wait_for_press()
        await button2.wait_for_release()
        print("Done")

    asyncio.run(main())
