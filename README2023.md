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

See the code at [e03_buttons.py](e03_buttons.py).

I discovered that the MicroPython thread module only supports one extra thread
other than the main thread. This is a bit limiting so for tomorrow I'm going to
take a look at asyncio. I was rather pleased to discover that MicroPython supports it, so we need to give that a whirl.

# Day 3 Project
Today we get two buttons. The PiHut instructions are
[here](https://thepihut.com/blogs/raspberry-pi-tutorials/let-it-glow-maker-advent-calendar-day-3-incredible-inputs)

Now what interesting things can we do with two buttons and two LEDs?.

I'm thinking that we should build a state machine controlled by the buttons,
that performs a variety of different actions. I'm going to use asyncio to
make everything nice and snappy.

Work in Progress ...
