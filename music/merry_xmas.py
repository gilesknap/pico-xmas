from utils.tune import Tune

# create tune for the song "wish you a merry christmas"
# each note is a tuple of (note, length, gap)
# or a string for print out of the lyrics!
wish_you_a_merry_xmas = [
    # We wish you a merry Christmas
    "We",
    (Tune.D, 0.5, 0.1),
    "wish",
    (Tune.G, 0.5, 0.1),
    "you",
    (Tune.G, 0.25, 0),
    "a",
    (Tune.A, 0.25, 0.02),
    "Merry",
    (Tune.G, 0.25, 0),
    (Tune.Fs, 0.25, 0.05),
    "Christmas",
    (Tune.E, 0.5, 0.1),
    (Tune.E, 0.5, 0.1),
    # We wish you a merry Christmas
    "We",
    (Tune.E, 0.5, 0.1),
    "wish",
    (Tune.A, 0.5, 0.1),
    "you",
    (Tune.A, 0.25, 0),
    "a",
    (Tune.B, 0.25, 0.02),
    "Merry",
    (Tune.A, 0.25, 0),
    (Tune.G, 0.25, 0.05),
    "Christmas",
    (Tune.Fs, 0.5, 0.1),
    (Tune.D, 0.5, 0.1),
    # and a happy new year!
    "and",
    (Tune.C, 0.25, 0.1),
    "a",
    (Tune.C, 0.25, 0.1),
    "happy",
    (Tune.D, 0.5, 0.1),
    (Tune.G, 0.5, 0.1),
    "new",
    (Tune.E, 0.5, 0.1),
    "year!",
    (Tune.F, 1, 0.1),
]
