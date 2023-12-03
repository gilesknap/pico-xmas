# This is a slightly more advanced version of
# https://thepihut.com/blogs/raspberry-pi-tutorials/let-it-glow-maker-advent-calendar-day-2-lighting-leds
# this version uses modules and threading to blink both leds simultaneously
# at a different rate.
#
# We have broken the code into modules like last year
# - hardware.advent2023.py defines the hardware wiring that we have
# - utils.led.py defines the Led class with 'blink' and other methods
# - utils.background defines the Background class that can run a function
#   in the background so we can blink both leds at the same time at different
#   rates

# Imports
from hardware.advent2023 import onboard_led, red_led
from utils.background import Background

secs  = 6

# worker function for the background thread
def red_blink():
    red_led.blink(period=0.5, secs=secs)

# create the background thread manager
red = Background()

# start the background thread
red.start(red_blink, repeat=False)

# blink the onboard led in the foreground
onboard_led.blink(period=0.3, secs=secs)

# NOTE: my first instinct was to use two thread objects but the pico
# only supports two threads and one of those is the foreground REPL
# so we have to use one thread object and run the other function in the
# in the foreground.
