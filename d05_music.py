from utils.tune import Notes, play_tune

# create tune for the song "wish you a merry christmas"
# each note is a tuple of (note, length, gap)
wish_you_a_merry_xmas = [
    (Notes.D, 0.5, 0.1),
    (Notes.G, 0.5, 0.1),
    (Notes.G, 0.5, 0.1),
    (Notes.A, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
    (Notes.C, 0.5, 0.1),
]

play_tune(wish_you_a_merry_xmas)
