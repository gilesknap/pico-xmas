import asyncio

from asyn.segmented import Segmented


async def main():
    # create the Segmented display object
    s = Segmented()
    # start the background task that will count up in binary on the display
    s.start_count()

    # just wait until the count is done
    await s.wait_for_done()


asyncio.run(main())
