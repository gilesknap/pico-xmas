import asyncio

from machine import PWM, Pin


class Led:
    """
    A class to represent an LED attached to a GPIO on the Pico.

    This is the async version of the Led class from utils/led.py
    """

    def __init__(self, pin_num):
        # initialize the LED to off and full brightness
        self.task = None
        self.pin = Pin(pin_num, Pin.OUT)
        self.pwm = PWM(self.pin)
        self.pwm.freq(1000)
        # full brightness
        self.power = 65535
        # turn the LED off
        self.pwm.duty_u16(0)

    def on(self):
        """turn on the LED at the current brightness"""
        self.pwm.duty_u16(self.power)

    def off(self):
        """turn off the LED"""
        self.pwm.duty_u16(0)

    def value(self, value):
        """set the LED on or off based on argument value"""
        if value:
            self.on()
        else:
            self.off()

    def brightness(self, value=65535):
        """set the brightness of the LED"""
        self.power = value
        # if the LED is already on then change the brightness
        if self.pwm.duty_u16() > 0:
            self.on()

    async def blink(self, period_ms):
        while True:
            self.on()
            await asyncio.sleep(period_ms * 0.001)
            self.off()
            await asyncio.sleep(period_ms * 0.001)

    def start(self, period_ms):
        self.task = asyncio.create_task(self.blink(period_ms))

    def stop(self):
        if self.task:
            self.task.cancel()

    def __repr__(self):
        """return a string representation of the LED"""
        return f"Led({self.pin})"
