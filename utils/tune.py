import time

from hardware.advent import buzzer


# Create our library of tone variables
class Notes:
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


# Create our function with arguments
def play_tone(note: int, length: int, gap: int, volume: int = 1000):
    buzzer.duty_u16(volume)
    buzzer.freq(note)
    time.sleep(length)
    buzzer.duty_u16(0)
    time.sleep(gap)


# play the sequence of tones
def play_tune(tune: list):
    for note, length, gap in tune:
        print(note, length, gap)
        play_tone(note, length, gap)

    # buzzer off
    buzzer.duty_u16(0)
