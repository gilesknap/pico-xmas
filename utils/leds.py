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

    def on(self, period=0.0):
        # turn on the LED at the current brightness
        self.pwm.duty_u16(self.power)

    def off(self):
        self.pwm.duty_u16(0)

    def value(self, value):
        # set the LED on or off based on argument value
        if value:
            self.on()
        else:
            self.off()

    def brightness(self, value=65535):
        self.power = value
        # if the LED is already on then change the brightness
        if self.pwm.duty_u16() > 0:
            self.on()

    def blink(self, period=0.5, count=1):
        for step in range(count):
            self.on()
            sleep(period)
            self.off()
            if step < count - 1:
                sleep(period)

    def __repr__(self):
        return f"Led({self.pin})"


# Set up our LED names and GPIO pin numbers
onboardLED = Led(25)
red = Led(18)
amber = Led(19)
green = Led(20)
