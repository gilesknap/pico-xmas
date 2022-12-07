"""
Configuration for interfacing with the Hardware supplied
in the PiHut Advent Calendar 2022

Note for my projects I have tried to use all components
simultaneously, so I have used different GPIO pins to the
ones in the PiHut instructions for the following items:

- Buzzer: GP12 physical pin 16
- pir_sensor: GP28 physical pin 35 (ADC2)
"""

from machine import ADC, PWM, Pin

from utils.led import Led

# Set up our LED names and GPIO pin numbers
onboardLED = Led(25)
red = Led(18)
amber = Led(19)
green = Led(20)

# Set up our button names and GPIO pin numbers
# Also set pins as inputs and use pull downs
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# Set up the Buzzer pin as PWM
# DIFFERENT FROM PiHut instructions!!
# OR use Pin(13) for the PiHut wiring
buzzer = PWM(Pin(12))  # Set the buzzer to PWM mode


# Define pin for light sensor
light_sensor = ADC(Pin(26))

# Define pin for PIR sensor
# DIFFERENT FROM PiHut instructions!!
# OR use Pin(26) for the PiHut wiring
pir_sensor = Pin(28, Pin.IN, Pin.PULL_DOWN)
