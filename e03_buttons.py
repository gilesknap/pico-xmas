import asyncio

from hardware.async2023 import green_button, onboard_led, red_button, red_led


class DoBlink:
    """
    A class to blink an LED in the background using asyncio.
    """

    def __init__(self, led, period_ms):
        self.led = led
        self.period_ms = period_ms
        self.task = None

    async def blink(self):
        while True:
            self.led.on()
            await asyncio.sleep(self.period_ms * 0.001)
            self.led.off()
            await asyncio.sleep(self.period_ms * 0.001)

    def start(self):
        self.task = asyncio.create_task(self.blink())

    def stop(self):
        if self.task:
            self.task.cancel()


# global values shared by the event handlers
MODE = 0  # 0 = solid, 1 = blinking
ENABLED = False
blink1 = DoBlink(onboard_led, 700)
blink2 = DoBlink(red_led, 400)


# callback function for red button, toggles modes when it is pressed
# and does nothing when it is released
def switch_mode(button):
    global MODE
    if button.pressed:
        if MODE == 0:
            print("blinking mode")
            MODE = 1
        else:
            MODE = 0
            print("solid mode")
        change_leds()


# a callback function for the green button, toggles the ENABLED flag when
# it is pressed and does nothing when it is released
def switch_enabled(button):
    if button.pressed:
        # don't switch enabled in here to demo use of asyncio Button functions
        # in main()
        print("toggle enable LEDs")


# a function for switching the LEDs state. Call this when mode or enabled
# flags have changed
def change_leds():
    blink1.stop()
    blink2.stop()
    if ENABLED:
        if MODE == 1:
            blink1.start()
            blink2.start()
        else:
            onboard_led.on()
            red_led.on()
    else:
        onboard_led.off()
        red_led.off()


# main function must be async to use asyncio features.
# this just sets up the buttons and monitors the green button for presses
# to toggle the ENABLED flag. The red button is monitored in the background
# by the Button class and calls the switch_mode callback function when it
# is pressed.
async def main():
    global ENABLED
    red_button(callback=switch_mode)
    go_button = green_button(callback=switch_enabled)

    while True:
        await go_button.wait_for_press()
        ENABLED = not ENABLED
        change_leds()
        await go_button.wait_for_release()


# launch the main function asynchronously
asyncio.run(main())
