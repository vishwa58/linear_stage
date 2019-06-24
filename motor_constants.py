import RPi.GPIO as GPIO #allows for use of GPIO pins

#This file constains all the constants fr the motor informatin and can be changed at will
#sets the step angle for the stepper motor
STEP_ANGLE = 1.8
#sets the number of microsteps per steps
MICROSTEPS_PER_STEP = 8
#sets the screw pitch of the lead screw in mm
SCREW_PITCH = 6
#Sets the pin used for the Direction Pin
DIR_PIN = 23
#Sets the pin used for the Pulse Pin
PULSE_PIN = 24
#Sets the pin for the limitswitch
LIMITSWITCH = 21
GPIO.setup(LIMITSWITCH, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#These represent the direction the motor will move. 
#If the stage is not moving in the correct direction either swap the stepper motor wires or swap these values.
# (Set HOME_DIRECTION to 1 and ETCHANT_DIRECTION to 0)
HOME_DIRECTION =0
ETCHANT_DIRECTION =1


#Set this value to true if there is an endstop
ENDSTOP_ENABLED = False

#This value represents the homing speed
HOMING_SPEED = .00004