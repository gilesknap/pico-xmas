import time

from hardware.advent import button1, button2, light_sensor, potentiometer
from music.merry_xmas import wish_you_a_merry_xmas
from utils.background import Background
from utils.count import BinCounter
from utils.tune import Tune

music = Tune(wish_you_a_merry_xmas, lyrics=True)
background_music = Background()

print("press button 1 to start and button 2 to stop")
while button1.value() == 0:
    time.sleep(0.1)

quiet = True

background_music.start(music.play_tune_once)

while button2.value() == 0:
    # Read sensor value and store it in a variable called 'light'
    light = light_sensor.read_u16()

    # Use the round function to limit the decimal places to 1
    light_percent = round(light / 65535 * 100, 1)

    # convert to a number between 0 and 15 for binary LED display!
    light_binary = round(light / 65535 * 15)

    # Print our reading percentage with % symbol
    if not quiet:
        print(f"light level is {light_percent}% = 0b{light_binary}")

    binary = BinCounter.to_binary(light_binary)
    BinCounter.show_binary_leds(binary)

    pot_value = potentiometer.read_u16()  # get the potentiometer value
    music.volume = pot_value  # set volume according to potentiometer

    time.sleep(0.1)

background_music.stop()
