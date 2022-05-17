# technic-42131

Physical remote control for LEGO Technic 42131: Cat D11 Bulldozer.

This is a short Pybricks program to control the Cat from a LEGO PU remote. Although it lacks the app's niceties such as tilt information, route drawing and especially proportional control, I found physical buttons more pleasant to use and it switches functions a lot faster (not to mention the calibration only takes a few seconds).

I based the code on Balazs Kiss' program for 42124 Off-Road Buggy, which in turn was based on Jorge Pereira's code.

In the program, I set the remote's +/- buttons to directly control the treads. The red buttons control the active function. Pressing the green button cycles through the four functions, and the remote's LED indicates which one is active:

* **Blue:** blade lift
* **Green:** ripper
* **Yellow:** ladder
* **Red:** blade tilt
* **White:** function switching in progress

To use: copy-paste the contents of main.py into the Pybricks IDE and either download it to the model or install it along with the firmware.

Video of the program in action at [YouTube](https://youtu.be/gy3nFvojZ2o).

This program served as inspiration for the 42131 project at [Pybricks.com](https://pybricks.com/projects/sets/technic/42131-cat-bulldozer/powered-up-remote/).
