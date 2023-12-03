from time import sleep

from machine import PWM, Pin


class Led:
    """
    A class to represent an LED attached to a GPIO on the Pico.
    """

    def __init__(self, pin_num):
        # initialize the LED to off and full brightness
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

    def blink(self, period=0.5, count=1, secs=0.0):
        """blink the LED for count times with period seconds between on and off"""
        if secs > 0:
            # calculate the number of blinks based on the period and secs
            count = int(secs / period)
            print(f"count = {count}")
        for step in range(count):
            self.on()
            sleep(period)
            self.off()
            # don't pause after the last blink
            if step < count - 1:
                sleep(period)

    def __repr__(self):
        """return a string representation of the LED"""
        return f"Led({self.pin})"
