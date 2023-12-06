import asyncio

from hardware.async2023 import segments


class Segmented:
    """
    A class to represent the 5 segment display from Advent Calendar 2023 day 4.

    It uses binary to represent the value of the display. The 5 segments can
    represent 0-31 (00000 to 11111 in binary).
    """

    def __init__(self):
        # use the segments list from hardware/async2023.py
        self.segments = segments
        self.bit_mask = []
        # prepare a list of tuples to represent binary 00000 to 11111
        for i in range(32):
            digits = tuple(int(d) for d in f"{i:05b}")
            self.bit_mask.append(digits)
        self.value = 0
        self.start = 0
        self.stop = 31
        self.step = 1
        self.task = None
        self.period_ms = 500

    def set_value(self, value):
        """set the value of the display"""
        self.value = value
        self.display()

    def display(self):
        """display the current value"""
        # get the bit mask for the current value
        mask = self.bit_mask[self.value]
        # set each segment to the appropriate value
        for i in range(5):
            self.segments[i].value(mask[i])

    async def _counter(self, repeats):
        for _ in range(repeats):
            for i in range(self.start, self.stop + 1, self.step):
                self.set_value(i)
                await asyncio.sleep(self.period_ms * 0.001)

    def start_count(self, start=0, stop=31, step=1, period_ms=500, repeats=5):
        self.start = start
        self.stop = stop
        self.step = step
        self.period_ms = period_ms
        self.task = asyncio.create_task(self._counter(repeats))

    def stop_count(self):
        if self.task:
            self.task.cancel()

    def __repr__(self):
        """return a string representation of the display"""
        return f"{self.value:05b})"
