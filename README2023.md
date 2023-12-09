2023 Let it Glow
================

Because it's 2023 I've added a bit of AI to the project. One of the configured
vscode extensions is CoPilot which is an AI assistant for coding. I use this
daily in my job and it does save me lot's of typing. It will work out
what you are trying to do and suggest code to do it. Just hit tab to accept the
suggestion.

To use it in this project you would need to sign up for CoPilot. You can read
about CoPilot
[here](https://code.visualstudio.com/blogs/2023/03/30/vscode-copilot).
and sign up for a free trial
[here](https://docs.github.com/en/copilot/using-github-copilot/getting-started-with-github-copilot?tool=vimneovim)

# Day 1 Project

This is about setting up the hardware and getting the tools installed.

We are using vscode for development and the MicroPico extension.
This replaces Thonny. See the main [README](README.md) for my instructions
on setting up vscode and the MicroPico extension.

The [pihut instructions](https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-1-getting-started).
discuss the hardware setup.

With the limited hardware for day one you could try the morse code project
if you did already do it. [See details here](README2022.md#day-1-project).

I needed to remind myself how to make this work. In fact it's probably changed
because @paulober has made some major improvements to the MicroPico vscode
extension. The file upload issues from last year are gone and the UI is
improved.

The steps are:

- right click in the explorer and select 'Upload Project to Pico'
- Select the file `d01_start_morse.py` and click on "> Run" on the status bar
  at the bottom of the screen.

You should see the message
- Playing 'happy christmas everyone   '
and the LED should flash.

# Day 2 Project

Today we got a big red diffuse LED.
PiHut instructions to install the hardware are
[here](https://thepihut.com/blogs/raspberry-pi-tutorials/let-it-glow-maker-advent-calendar-day-2-lighting-leds).

For today I again reused some of the modules from last year. We have made the
new LED and the onboard LED flash simultaneously at different rates using
MicroPython's `_thread` module.

See the code at [e02_led.py](e02_led.py).

I discovered that the MicroPython thread module only supports one extra thread
other than the main thread. This is a bit limiting so for tomorrow I'm going to
take a look at asyncio. I was rather pleased to discover that MicroPython supports it,
so we need to give that a whirl.

# Day 3 Project
Today we get two buttons. The PiHut instructions are
[here](https://thepihut.com/blogs/raspberry-pi-tutorials/let-it-glow-maker-advent-calendar-day-3-incredible-inputs)

IMPORTANT: I have used pin 0 and 1 instead of 2 and 3 as the instructions,
this is so I can fit everything up to day 5 on the board at once. If you want
to use my code you should do the same, or change the values for Red and
Green buttons in [hardware/async2023.py](hardware/async2023.py).

To use my code unchanged plug the red button into physical pin 0 and the green button
into physical pin 1. This is instead of pins 4 and 5 as in PiHut instructions.

OK that took way longer than expected as I got caught up in finding out
how interrupts work in MicroPython. It's a bit weird because interupts on
one pin seem to get reported on other pins as well *sometimes*. However I was
able to eliminate any crosstalk by keeping the button state and only executing
actions on transitions from pressed to released or vice versa.

Today's code demonstrates how to use interrupts to detect button presses. But
also how to do background tasks using asyncio. So we have two different methods
of parallel processing in the same project.

If you run this code you should find that:

- The green button enables and disables both LEDs
- the red button toggles between flashing the LEDs and just having them on.


See [e03_buttons.py](e03_buttons.py).

# Day 4 Project
Today we added a 5 segment display. Hardware Setup is
[here](https://thepihut.com/blogs/raspberry-pi-tutorials/let-it-glow-maker-advent-calendar-day-4-brilliant-bar-graphs)

For today I have continued in the theme of using asyncio to do
background processing. I created a class in [segmented.py](asyn/segmented.py)
that represents the interface to the relevant pins and allows us to
do background counting in binary.

The code that uses the new module is [e04_segmented.py](e04_segmented.py) don't
forget to upload the project before running this file as it relies on the
above module which would not yet be on your pico.

Today I also tidied up the look of my breadboard by purchasing a jumper
cable kit. The one I used was £6.99 from
[Amazon](https://www.amazon.co.uk/dp/B08PF2W1RF?psc=1&ref=ppx_yo2ov_dt_b_product_details)
and it works quite well.

This makes the board a bit more reliable because the cables don't get knocked out as
easily.

Here is the result, you may notice that I inverted the segmented LED to make the wiring
tidy. (The mapping from PIN to segment when viewed up this way is the same as it was)

![image](https://github.com/gilesknap/pico-xmas/assets/964827/46e64c0b-d565-4e86-ac5d-ab2e23c94b1d)

# Day 5 Project
Today we add a dip switch. I'm trying to keep all the components wire on the
board so I have moved the dip switch over to the left of the two buttons.

The wiring set up is still the same as the PiHut instructions
[here](https://thepihut.com/blogs/raspberry-pi-tutorials/let-it-glow-maker-advent-calendar-day-5-switch-the-dip)

I've not written any new code for these. But planning on making a project that
uses as many of the items at once as far as possible.

# Day 6 Project
Today we get two RGB LEDs. To keep everything so far I have added the breadboard
from last year below the pico. I'm installing the RGB LEDs on that breadboard.

To allow this I have connected their GPIO inputs to GPIO27 and GPIO28. These
are physical pins 34 and 32. The remaining pins are connected as per the PiHut
instructions
[here](https://thepihut.com/blogs/raspberry-pi-tutorials/let-it-glow-maker-advent-calendar-day-6-see-the-rgb)

See the image below for the details of the wiring. From this point on I'm using an
extra breadboard from last year's kit. This is so I can fit all the components in
without removing any previous days parts. If you don't have a spare board and
want to follow along you could pick one up for £4 on
[Amazon](https://www.amazon.co.uk/400-Point-Solderless-PCB-Breadboard/dp/B013EW663K/ref=sr_1_18?keywords=breadboard&qid=1702119593&sr=8-18)

My code today is a simple single threaded script that pulses the lights
in a fashion that I found pleaseing. see [e05_rgb.py](e05_rgb.py)

![image](https://github.com/gilesknap/pico-xmas/assets/964827/1ecd304d-c378-47de-8994-b300e753e157)

# Day 7 Project
Today we get a sliding potentiometer. For today I'm just using PiHut's
code because I'm working on the 'all things' project.

Note, due to keeping everything on the board I have used GPIO 26 instead of
GPIO 25 as in the PiHut instructions.

See PiHut instructions
[here](https://thepihut.com/blogs/raspberry-pi-tutorials/let-it-glow-maker-advent-calendar-day-7-time-to-slide)

My code with the change to GPIO 26 is [e06_pot.py](e06_pot.py)

# Day 8 Project
Today we get a ring of RGB LEDs.

Here I'm connecting the ring control to GPIO15 physical pin 20
instead of GPIO2.

# Day 9 Project
Today we get a temp and humidity sensor.

I'm using GP19 (physical pin 25) for I2C SCL and GP18 (physical pin 24) for
I2C SDA.
