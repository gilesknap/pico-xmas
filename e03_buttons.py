import asyncio

from hardware.async2023 import green_button, onboard_led, red_button, red_led


class DoBlink:
    def __init__(self, led, period_ms):
        self.running = False
        self.led = led
        self.period_ms = period_ms

    async def blink(self):
        while self.running:
            self.led.on()
            await asyncio.sleep(self.period_ms * 0.001)
            self.led.off()
            await asyncio.sleep(self.period_ms * 0.001)

    def start(self):
        self.running = True
        self.task = asyncio.create_task(self.blink())

    def stop(self):
        self.running = False


# global values shared by the event handlers
MODE = 0  # 0 = solid, 1 = blinking
ENABLED = False
blink1 = DoBlink(onboard_led, 700)
blink2 = DoBlink(red_led, 400)


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


def switch_enabled(button):
    if button.pressed:
        # don't switch enabled in here to demo use of asyncio Button functions
        # in main()
        print("toggle enable LEDs")


def change_leds():
    blink1.stop()
    blink2.stop()
    onboard_led.on()
    red_led.on()
    if ENABLED:
        if MODE == 1:
            blink1.start()
            blink2.start()
    else:
        onboard_led.off()
        red_led.off()


async def main():
    global ENABLED
    red_button(callback=switch_mode)
    go_button = green_button(callback=switch_enabled)

    while True:
        await go_button.wait_for_press()
        ENABLED = not ENABLED
        change_leds()
        await go_button.wait_for_release()


asyncio.run(main())
