import time

from utils.count import BinCounter


def count_led(iterations=15, pause=0.5, forwards=True, silent=False):
    start_time = time.time()  # Get the current time

    counter = BinCounter(forwards=forwards, silent=silent)

    for num in range(iterations):  # Loop 16 times
        counter.count_led()  # Count one
        time.sleep(pause)

    interval = time.time() - start_time  # Calculate the time taken
    print(f"Counted {iterations} times in {interval} seconds")


count_led()
