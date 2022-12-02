from time import sleep

from machine import Pin

# Set up our LED names and GPIO pin numbers
onboardLED = Pin(25, Pin.OUT)
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)


def led_on(period=0.0):
    onboardLED.value(1)
    if period > 0:
        sleep(period)
        led_off()


def led_off():
    onboardLED.value(0)
