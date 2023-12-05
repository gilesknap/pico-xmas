import asyncio

from hardware.async2023 import green_button, onboard_led, red_button, red_led


async def blink(led, period_ms):
    while True:
        led.on()
        await asyncio.sleep(0.005)
        led.off()
        await asyncio.sleep(period_ms * 0.001)


async def main(led1, led2):
    asyncio.create_task(blink(led1, 700))
    asyncio.create_task(blink(led2, 400))
    await asyncio.sleep(30)


asyncio.run(main(onboard_led, red_led))
