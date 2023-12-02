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

Followed by a reboot (logout is not enough)

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
For this project I have used vscode with this extension
https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go.

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


I've now broken the README up into the the two separate years:

- [2022 The 12 Projects of Codemas](README2022.md)
- [2023 Let it Glow](README2023.md)

