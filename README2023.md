2023 Let it Glow
================

Because it's 2023 I've added a bit of AI to the project. One of the configured
vscode extensions is CoPilot which is an AI assistant for coding. I use this
daily in my job and it does save me lot's of typing. It will work out
what you are trying to do and suggest code to do it.

To use it in this project you would need to sign up for CoPilot. You can read
about CoPilot
[here](https://code.visualstudio.com/blogs/2023/03/30/vscode-copilot).
and sign up for a free trial
[lhere](https://docs.github.com/en/copilot/using-github-copilot/getting-started-with-github-copilot?tool=vimneovim)

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
- right click on the file `d01_start_morse.py` and select
  'Run current file on Pico'

You should see the message
- Playing 'happy christmas everyone   '
and the LED should flash.
