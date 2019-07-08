# Variable Speed Linear Stage

This piece of software was written by Vishwa Nathan (vnathan@umich.edu) while he was working as a research assistant in the Burns Lab (http://cheresearch.engin.umich.edu/burns/) at the University of Michigan. The purpose of this project was to control a linear stage using three different velocity profiles: constant velocity, linearly increasing velocity and exponentially increasing velocity. These velocity profiles in conjunction with the linear stage are used to create variable depth glass etchings for use in microfluidic devices.

## Getting Started

These instructions will get the user a copy of the project on their Raspberry Pi.

## Prerequisites
The following guide assumes that the following prerequisities have been met

```
The user has a working Raspberry Pi with Python 3 installed

The user has read the "Variable Speed Linear Stage Software and Electronics Documentation" if they intend to utilize the hardware found in this project as well

```
## Contents

The following code is broken up into 4 major files
1. linear_stage_functions.py 
    This file contains all the helper functions that interface with the hardware to control the linear stage. If the user is only trying to run the linear stage, this file should not be changed.
2. motor_constants.py
    This file contains all the constants related to the hardware as well as some software constants. Information regarding Raspberry Pi GPIO pins are          found here. The user is welcome to change the information found in this file to suit their needs.
3. gui_layout.py
    This file uses the tkinter library and contains the code for the user interface. If the user is only trying to run the linear stage, this file should not    be changed.
4. run_linear_stage.py
    This file contains the code that links the backend and the frontend of the linear stage code. If the user is only trying to run the linear stage, this file should not be changed.

## Installing


1. Navigate to the following link
    https://github.com/vishwa58/linear_stage.git
2. Click the green button that says “clone or download”
3. Press the button that says “Download Zip”
4. A folder should have been downloaded to the Pi named “linear-stage-master”(if it is a zip file, unzip the folder first)
5. Move this folder into the Documents folder (This will be the working directory. More advanced users can use the working directory of their choosing.)
6. Navigate to the working directory 

    If you do not know what a working directory is, type the following commands (assuming you saved the folder in documents)

```
cd ~
cd Documents/linear-stage-master/
```
7. To run the linear stage, type the following command into the terminal. (Assuming the user has already navigated to the working directory). Make sure to use the python3 command and not python.

```
python3 run_linear_stage.py

```

For a more complete guide including images, please refer to "Variable Speed Linear Stage Software and Electronics Documentation" 


 
## Built With

* [Tkinter](https://docs.python.org/3/library/tkinter.html) - The python framework used for the user interface.

## Acknowledgments

* Thank you to Martin de Beer (mapadebe@umich.edu) for contributing to the overall outline of this code.
* Thank you to Eric Viscione (ericjviscione@gmail.com) for answering any and all hardware related questions.
* Thank you to Cam Bortolussi (cambortolussi44@gmail.com) for creating the graphics for the user interface.


