2022 The 12 Projects of Codemas
===============================

# Day 1 Project
These projects are split into multiple modules for reuse and readability.
First upload all the project files. Then execute the desired numbered entry
module e.g. d01_start_morse.py.

[Hardware setup for day 1](https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-1-getting-started)

Play any phrase in morse code on the onboard LED.

Code [d01_start_morse.py](01_start_morse.py)

# Day 2 Project

[Hardware setup for day 2](https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-2-let-s-get-blinky)

Repeatedly count up to 15 in binary using the 3 LEDS and on board LED to represent bits as
follows

- RED = 8
- AMBER = 4
- GREEN = 2
- ONBOARD = 1

Code [d02_count.py](d02_count.py)

# Day 3 Project

[Hardware setup for day 3](https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-3-bashing-buttons)

Light combinations of LEDs through combinations of button presses.

Code [d03_buttons.py](d03_buttons.py)

# Day 4 Project

[Hardware setup for day 4](https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-4-amazing-analogue)

Today I have combined the potentiometer and switches onto a single breadboard which is a little deviation from
the PiHut instructions. My changes are:

- move the switches up to one end of the board to make room
- also move their wires accordingly
- put the potentiometer at the other end of the board and wire as per PiHut, except
- take the 3.3v power from the power rail on the left of the main board.

See this image for details

![image](https://user-images.githubusercontent.com/964827/205515981-920f1e4e-72ad-4f05-aceb-f9c60e8026f9.png)

This project combines everything we have used so far plus demos a few more advanced features of MicorPython:
- multi threaded code
- use of classes

Description:

    Run a Binary counter that lights 4 LEDs in a background thread.
    Monitor inputs to control the counters follows:

    button 1: toggle between speed and brightness control
    button 2: toggle direction of the counter
    button 3: terminate the program
    potentiometer: control speed or brightness depending on the mode set by button 1



Code [d04_controller.py](d04_controller.py)


# Day 5 Project

[Hardware setup for day 5](https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-5-hear-my-code)

Today I have encoded the song 'We Wish You a Merry XMas' with lyrics using
a list and tuples.

I used [this page](https://www.bethsnotesplus.com/2014/07/we-wish-you-merry-christmas.html)
to populate the list of notes.

Perhaps someone more musical than I would like to contribute the rest of the
song?

Code [d05_music.py](d05_music.py)

# Day 6 Project

[Hardware setup for day 6](https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-6-looking-for-light)

Today I have combined the new light sensor with everything from previous days.

To do this you need to cram all of the components on the same breadboard.
I'm pretty sure I'm going to run out of space if I try to keep this up until
day 12.

I'll leave it up to you to work out how to do the component layout, but will
enclose a picture of mine to give an idea of how to do it.

Today's code does the following:

- Monitors the light level
- Converts light level to a 4 bit value (0 - 15)
- Displays the light level in binary on the 4 LEDs
- Plays 'We Wish You a Merry XMas'
- With Lyrics!
- With volume controlled by the potentiometer
- Uses buttons to start and stop everything


Code [d06_photo_t.py](d06_photo_t.py)
![image](https://user-images.githubusercontent.com/964827/206023165-11f5ab33-420a-4482-8de1-34b1f8645e5c.png)

# Day 7 Project

[Hardware setup for day 7](https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-7-monitoring-motion)

Today I've just pretty much copied the alarm code from PiHut. I thought it would
be interesting to give the alarm a disarm code to punch in on the buttons,
but no time today.

I have still crammed all the components on to the existing breadboard and
had to use ADC2 (pin 28) instead of pin 31. I moved the switches to one side of
the mini-board to make space.

Code [d07_pir.py](d07_pir.py)
