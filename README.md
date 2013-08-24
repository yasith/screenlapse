screenlapse
===========
0.0.0

A really simple command line tool for generating time lapse videos of your desktop on the mac.

This will create a directory "~/screencaps" if it does not exist, then save a sequence of png files in that directory named "screenXXXXXXXXXX.png", starting with "screen0000000000.png" and incrementing the number each captured frame. It will take
a new screenshot every second.

Later version will have command line arguments allowing you to configure the screenshot name, frequency, directory and so on.

You need python (the instructions assume you've installed python 3.3+ through homebrew). Just clone this repository, and from that directory type "python3 screenlapse.py" and it will begin capturing.

To create a video from the screen captures, you need ffmpeg (again, I installed through homebrew), just type "python3 makevideo.py" and it will create a .m4v file named "timelapse.m4v".

