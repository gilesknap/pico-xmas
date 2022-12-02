# timings for morse code
# See https://morsecode.world/international/timing.html
wpm = 13  # words per minute (for the reference word PARIS)
dit = 1200 / wpm * 0.001  # 1200ms / 25 dits = 92ms
dah = dit * 3
dit_space = dit
char_space = dit * 3
word_space = dit * 7

# morse code dictionary
# from https://www.sciencegateway.org/gr/morse.htm
code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}
