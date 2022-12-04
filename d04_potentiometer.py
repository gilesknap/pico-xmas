# Imports (including PWM and ADC)
import time

from machine import ADC, PWM, Pin

from utils.count import BinCounter

# get all the GPIO pins used for the LEDs
all_leds = BinCounter.led_bits
all_pw

# Set the PWM Frequency for all LED pins
# Sets how often to switch the power between on and off for the LED
for led in all_leds:
    pwm = PWM(led)
    pwm.freq(1000)


b = BinCounter()
b.start()

while True:  # Run forever

    reading = (
        potentiometer.read_u16()
    )  # Read the potentiometer value and set this as our reading variable value

    print(reading)  # Print the reading

    # Set the LED PWM duty cycle to the potentiometer reading value
    # The duty cycle tells the LED for how long it should be on each time
    led.duty_u16(reading)

    time.sleep(0.01)
