from linear_stage_functions import *
import time
#from time import sleep #imports sleep function
#import RPi.GPIO as GPIO #allows for use of GPIO pins

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
newstepper = stepper(1.8, 1, 6, 24, 23, 1600)


#test constructor
print(newstepper.step_angle)
print(newstepper.mstep_per_step)
print(newstepper.screw_pitch)
print(newstepper.pulse_pin)
print(newstepper.dir_pin)
print(newstepper.steps_per_rev)

#test linear_velocity calculations
x = calculate_delay(12.85, newstepper)
print (x)
#x equals 80

#tests runmotor function

#x is from previous test for delay
y =0
start = time.time() #Takes the current time
while(y<newstepper.steps_per_rev):
    runmotor(newstepper,x)
    y=y+1
end = time.time()
print(end-start) #tells the suer how long it took for the motor to turn one revolution

#this is the calculate rotations test


#seehow the number of rotations it will take to move 30 cm
print(calculate_rotations(newstepper, 1200, 900))



#calculating overall_program
start = time.time()
const_velocity_movement(.0003, .007, 1200, 900, newstepper)
end = time.time()
print(end-start)



#test _position vector creation


newlist = create_Yc_vector(90, 120, mystepper)
print (*newlist, sep = "\n")

    











