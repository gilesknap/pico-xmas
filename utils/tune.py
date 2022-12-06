import time

from hardware.advent import buzzer


class Tune:
    """
    A class to play tunes on the buzzer
    """

    # Create our library of tone variables
    A = 440
    As = 466
    B = 494
    C = 523
    Cs = 554
    D = 587
    Ds = 622
    E = 659
    F = 698
    Fs = 740
    G = 784
    Gs = 830

    def __init__(self, tune: list, volume: int = 1000, lyrics=True):
        """setup a Tune object with a list of notes and a volume"""
        self.tune = tune
        self.volume = volume
        self.lyrics = lyrics

    def play_tone(self, note: int, length: int, gap: int):
        """play a tone for a given length of time and pause afterwards"""
        buzzer.duty_u16(self.volume)
        buzzer.freq(note)
        time.sleep(length)
        buzzer.duty_u16(0)
        time.sleep(gap)

    def play_tune_once(self):
        """play a tune"""
        for element in self.tune:
            if isinstance(element, str) and self.lyrics:
                print(element)
            elif isinstance(element, tuple):
                note, length, gap = element
                self.play_tone(note, length, gap)

        # buzzer off
        buzzer.duty_u16(0)

    def repeat_tune(self, repeat: int = 1):
        """play a tune a given number of times"""
        for _ in range(repeat):
            self.play_tune_once()
