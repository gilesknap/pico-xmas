# Imports (including PWM and ADC)
import time

from utils.count import BinCounter
from utils.inputs import button1, button2, button3, potentiometer

# get all the GPIO pins used for the LEDs
all_leds = BinCounter.led_bits


# Modes for the action of the potentiometer (no Enum in MicroPython)
class PotModes:
    Brightness = 0
    Speed = 1


class Controller:
    """
    Run a Binary counter in the background and monitor inputs to control the counter
    as follows:

    button 1: toggle between speed and brightness control
    button 2: toggle direction of the counter
    button 3: terminate the program
    potentiometer: control speed or brightness depending on the mode set by button 1
    """

    def __init__(self):
        self.mode = PotModes.Speed  # set the initial mode
        self.running = False

        # create an instance of the Binary Counter class and run it in the background
        self.counter = BinCounter()
        self.counter.start()

    def await_release(self, button):
        # use this to debounce the buttons
        while button.value():
            time.sleep(0.1)

    def run(self):
        self.running = True
        while self.running:

            pot_value = potentiometer.read_u16()  # get the potentiometer value

            # perform the analogue action depending on the mode
            if self.mode == PotModes.Speed:
                # speeds from 2/sec to 500/sec (+1 avoids div by zero)
                thousand_values = pot_value / 65535 * 1000 + 1
                self.counter.pause = 2 / thousand_values
            elif self.mode == PotModes.Brightness:
                # set the brightness of the LEDs
                for led in all_leds:
                    led.brightness(pot_value)

            # change the mode when button1 is pressed
            if button1.value():
                if self.mode == PotModes.Speed:
                    print("Brightness mode")
                    self.mode = PotModes.Brightness
                else:
                    print("Speed mode")
                    self.mode = PotModes.Speed
                self.await_release(button1)

            # change the direction when button2 is pressed
            if button2.value():
                print("Toggle direction")
                self.counter.forwards = not self.counter.forwards
                direction = "forwards" if self.counter.forwards else "backwards"
                print(f"Direction is now {direction}")
                self.await_release(button2)

            # terminate the program when button3 is pressed
            if button3.value():
                print("Stopping everything")
                self.counter.stop()
                self.running = False
                self.await_release(button3)

            time.sleep(0.1)  # Short Delay


c = Controller()
c.run()
