"""
A class to run a worker function in the background.
"""
import time
from _thread import start_new_thread


class Background:
    def __init__(self):
        self._running = False
        self._repeat = True
        # set this public variable to change the speed of the worker loop
        self.pause = 0.5

    def _runner(self):
        # the worker loop
        while self._running:
            self._function()
            if not self._repeat:
                self._running = False
            time.sleep(self.pause)

    def start(self, function, repeat=True, pause=0.5):
        # start the worker running in the background
        print("Starting background task")
        self._running = True
        self._repeat = repeat
        self._function = function
        self.pause = pause
        start_new_thread(self._runner, ())

    def stop(self):
        # cause the worker loop to exit
        print("Stopping background task")
        self._running = False
