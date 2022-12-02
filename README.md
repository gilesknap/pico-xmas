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
Note that some of the functions require you hit ctrl-shift-P and type 'pico'

![image](https://user-images.githubusercontent.com/964827/205357295-423a5b94-c466-457b-9a7d-2a4a2993d984.png)


# Day 1 Project
These projects are split into multiple modules for reuse and readability.
First upload all the project files. Then execute the desired numbered entry
module e.g. 01_start_morse.py.

[Hardware setup for day 1](https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-1-getting-started)

Play any phrase in morse code on the onboard LED.

Code [01_start_morse.py](01_start_morse.py)

# Day 2 Project

[Hardware setup for day 2](https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-2-let-s-get-blinky)

Repeatedly count up to 15 in binary using the 3 LEDS and on board LED to represent bits as
follows

- RED = 8
- AMBER = 4
- GREEN = 2
- ONBOARD = 1

Code [02_count.py](02_count.py)
