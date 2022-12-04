from machine import ADC, PWM, Pin

# Set up our button names and GPIO pin numbers
# Also set pins as inputs and use pull downs
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))
