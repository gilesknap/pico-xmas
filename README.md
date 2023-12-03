# pico-xmas
giles' projects for the RaspberryPi Pico from the XMas Advent Calendar 2022.

**Now with updates for the 2023 calendar 'Let it Glow'**
See https://thepihut.com/pages/maker-advent-2023-guides for the 2023 let it glow
projects.

See https://thepihut.com/pages/maker-advent-2022-guides for details of the
2022 projects.

## Setup
Note to make this work on linux requires:
```bash
sudo adduser <your_user_name> dialout
```

Followed by a reboot (logout is not enough). This group membership gives your
user access to the USB serial port that the PICO uses to communicate with the
host.

## Install MicroPython

My 2023 RPI Pico H came without microPython installed. To install it without
getting involved with Thonny I used the following steps:

Go here and download the latest UF2 file:
https://micropython.org/download/RPI_PICO/

Plug in your PICO while holding the BOOTSEL button. You will find that it
opens as a USB drive. Copy the above UF2 file to the drive and wait for it to
reboot.

Using this step after setting `dialout` group membership I was found that
the vscode extension attached immediately as soon as the PICO rebooted.

## Recommended developer tools
For this project I have used vscode which is an excellent integrated
development environments that supports working with any programming language
that you choose. To get vscode installed see
https://code.visualstudio.com/download

To work with vscode, the RPI Pico and MicroPython, this excellent plugin
makes everything work together nicely:
https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go.

It gives quite a nice experience compared to Thonny (see below).
If you clone this project it already includes the necessary extensions when
opened in vscode.

Note that you can access the functions of the extension using the new
commands that appear in the vscode status like this:
![image](https://user-images.githubusercontent.com/964827/205506367-4db0adbb-f2d7-437a-9ea3-e02ca7f5e977.png)

- With a pico project open you should automatically get a terminal linked to
  the pico when you plug it in to USB.
- To upload the project to your pico or execute right click on the 'pico-xmas'
  project folder in the explorer (pane to the left of the screen )and select
  'Upload project to the Pico'.
- To run your code, select the file you want to run and click the '> Run' button
  on the status bar at the bottom.

UPDATE: all issues with uploading code to the Pico seem to have been solved
since 2022 and everything works smoothly. If the extension does seem to stop
working, usually ctrl-C will help, but when
it does not use the Hard Reset function from 'All Commands' on the
vscode status bar.

![image](https://user-images.githubusercontent.com/964827/205357295-423a5b94-c466-457b-9a7d-2a4a2993d984.png)

I've now broken the README up into the the two separate years:

- [2022 The 12 Projects of Codemas](README2022.md)
- [2023 Let it Glow](README2023.md)

