from time import sleep

from machine import Pin

onboardLED = Pin(25, Pin.OUT)


def led_on(period=0.0):
    onboardLED.value(1)
    if period > 0:
        sleep(period)
        led_off()


def led_off():
    onboardLED.value(0)
