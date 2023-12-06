import asyncio

from asyn.segmented import Segmented


async def main():
    # create the Segmented display object
    s = Segmented()
    # start the background task that will count up in binary on the display
    s.start_count()

    # just wait for a long time and let the background task do its thing
    await asyncio.sleep(60000)


asyncio.run(main())
