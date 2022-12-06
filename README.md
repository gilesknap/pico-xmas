# pico-xmas
giles' projects for the RaspberryPi Pico from the XMas Advent Calendar 2022.

See https://thepihut.com/pages/advent for details of the projects.

## Setup
Note to make this work on linux requires:
```bash
sudo adduser <your_user_name> dialout
```

Followed by a reboot (logout is not enough)


## Recommended developer tools
For this project I have used vscode with this extension https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go.

This gives quite a nice experience compared to Thonny (see below).
If you clone this project it already includes the necessary extensions when
opened in vscode.

Note that you can access the functions of the extension using the new
commands that appear in the vscode status like this:
![image](https://user-images.githubusercontent.com/964827/205506367-4db0adbb-f2d7-437a-9ea3-e02ca7f5e977.png)

- With a pico project open you should automatically get a terminal linked to
  the pico when you plug it in to USB.
- To upload the project to your pico or execute a single file use right click
  in the project explorer. You will see two new options 'Run Current File' and
  'Upload Project'
- To start your own new project ctrl-shift-P -> Pico-W-Go -> Configure Project.

WARNING: there seems to be a bug with upload hanging when sending lots of files
to get around this simply hit ctrl-C while focused on the Terminal Window when
you see the upload process stick on a file. If you keep this up, all the files
will upload OK.

WARNING: occasionally things stop working. Usually ctrl-C will help, but when
it does not use the Hard Reset function from 'All Commands' on the
vscode status bar.

![image](https://user-images.githubusercontent.com/964827/205357295-423a5b94-c466-457b-9a7d-2a4a2993d984.png)


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

