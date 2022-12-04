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


