from utils.tune import Notes, play_tune

# create tune for the song "wish you a merry christmas"
# each note is a tuple of (note, length, gap)
# or a string for print out of the lyrics!
wish_you_a_merry_xmas = [
    # We wish you a merry Christmas
    "We",
    (Notes.D, 0.5, 0.1),
    "wish",
    (Notes.G, 0.5, 0.1),
    "you",
    (Notes.G, 0.25, 0),
    "a",
    (Notes.A, 0.25, 0.02),
    "Merry",
    (Notes.G, 0.25, 0),
    (Notes.Fs, 0.25, 0.05),
    "Christmas",
    (Notes.E, 0.5, 0.1),
    (Notes.E, 0.5, 0.1),
    # We wish you a merry Christmas
    "We",
    (Notes.E, 0.5, 0.1),
    "wish",
    (Notes.A, 0.5, 0.1),
    "you",
    (Notes.A, 0.25, 0),
    "a",
    (Notes.B, 0.25, 0.02),
    "Merry",
    (Notes.A, 0.25, 0),
    (Notes.G, 0.25, 0.05),
    "Christmas",
    (Notes.Fs, 0.5, 0.1),
    (Notes.D, 0.5, 0.2),
    # and a happy new year!
    "and",
    (Notes.C, 0.25, 0.1),
    "a",
    (Notes.C, 0.25, 0.1),
    "happy",
    (Notes.D, 0.5, 0.1),
    (Notes.G, 0.5, 0.1),
    "new",
    (Notes.E, 0.5, 0.1),
    "year!",
    (Notes.F, 1, 0.1),
]

play_tune(wish_you_a_merry_xmas)
