import time

from hardware.advent import light_sensor
from utils.count import BinCounter

while True:  # Run forever

    # Read sensor value and store it in a variable called 'light'
    light = light_sensor.read_u16()

    # Use the round function to limit the decimal places to 1
    light_percent = round(light / 65535 * 100, 1)

    # convert to a number between 0 and 15 for binary LED display!
    light_binary = round(light / 65535 * 15)

    # Print our reading percentage with % symbol
    print(f"{light_percent}% = 0b{light_binary}")

    binary = BinCounter.to_binary(light_binary)
    BinCounter.show_binary_leds(binary)

    time.sleep(0.1)
