# This file contains all of the functions that allow the motor to be controlled

from time import sleep #imports sleep function
import RPi.GPIO as GPIO #allows for use of GPIO pins
from math import log #allows for log
GPIO.setwarnings(False) #Turns off unnecessary warnings provided by Raspberry Pi





GPIO.setmode(GPIO.BCM) #uses BCM mode for pin layout (Don't change)

#These represent the direction the motor will move. 
#If the stage is not moving in the correct direction either swap the stepper motor wires or swap these values.
# (Set HOME_DIRECTION to 1 and ETCHANT_DIRECTION to 0)
HOME_DIRECTION =0
ETCHANT_DIRECTION =1

#Connects the limitswitch to GPIO 21. Change this value if you connected the motor to a different ouput pin
LIMITSWITCH = 21

#sets up the limitswitch as an input pin and sets its default statw to untriggered
GPIO.setup(LIMITSWITCH, GPIO.IN, pull_up_down = GPIO.PUD_UP)


#STEPPER MOTOR CLASS

#Creates a stepper motor class. This class takes in the step_angle, leadscrew pitch, the output pins for pulse and
#direction as well as the steps  per revolution for the motor. This way we can keep track of all the variables associated with
#the stepper in one place. 

class stepper:
    def __init__(self, step_angle, screw_pitch, pulse_pin, dir_pin, msteps):
        self.step_angle = float(step_angle)
        self.screw_pitch = float(screw_pitch)
        self.pulse_pin = int(pulse_pin)
        self.dir_pin = int(dir_pin)
        self.steps_per_rev = int((360/step_angle)*msteps)
        self.msteps = int(msteps)
        GPIO.setup(int(pulse_pin), GPIO.OUT)
        GPIO.setup(int(dir_pin), GPIO.OUT)

        
#Calculates the pulse delay which in turn controls the speed og the motor.
#Based on this equation
        #Linear velocity = (screw pitch * pulse_frequency)/ (steps per revolution of stepper motor)
#Rearranged to solve for pulse pulse_frequency
#delay = 1/pulse frequency

def calculate_delay(linear_velocity, mystepper):
    numerator = linear_velocity * mystepper.steps_per_rev 
    denominator = mystepper.screw_pitch
    pulse_freq = numerator/denominator
    delay = 1.0/pulse_freq
    return delay



#This function turns the stepper motor one step
# def runmotor(mystepper, delay):
#     GPIO.output(mystepper.dir_pin, 1)
#     GPIO.output(mystepper.pulse_pin,1)
#     sleep(delay)
#     GPIO.output(mystepper.pulse_pin,0)
#     sleep(delay)


#Moves the motor one step (helper function)

def runmotor(mystepper, delay, direction):
    GPIO.output(mystepper.dir_pin, direction) #sets direction of motor
    GPIO.output(mystepper.pulse_pin,1) 
    sleep(delay) 
    GPIO.output(mystepper.pulse_pin,0) 
    sleep(delay)

#Homes the linear stage towards the endstop and then moves it four full revolutions away from the endstop to prevent retriggering
def home(mystepper, limitswitch_pin):
    while(GPIO.input(limitswitch_pin)==True): #run the motor while the endstop is not pressed
        runmotor(mystepper, .00001, HOME_DIRECTION)
    GPIO.output(mystepper.pulse_pin, 0)
    for x in range(0, 4*mystepper.steps_per_rev): #move the motor in the opposite direction so that it does mot retrigger endstop
        runmotor(mystepper, .0003, ETCHANT_DIRECTION)



#wrapper function that allows has an input for the distance (used for the move buttonsin the gui)       
def movedistance(mystepper, delay, direction, distance):
    for x in range (0, distance):
        runmotor(mystepper, delay, direction)



#helper functioon to calculate change in position
def delta_position(final_position, initial_position):
    return (abs(final_position-initial_position))


#This function calculates the number of rotations the stepper motor will have to make in order to move the linear stage from
#the initial position to the final position
def calculate_rotations(mystepper, initial_position, final_position):
    delta_pos = delta_position(final_position,initial_position) #calculates distance the stage must move
    num_rotations = delta_pos/(mystepper.screw_pitch) #divides the total distance by the screw pitch to aquire the proper number of rotations
    return num_rotations


#Creates a list of every position that the linear stage will be at       
def create_Yc_vector(initial_position, final_position, mystepper):
    total_rotations = calculate_rotations(mystepper, initial_position, final_position) #calculates rotations
    num_steps = int(total_rotations * mystepper.steps_per_rev) #calculates number of total steps by multiplying num rotations by steps per rotation
    position_list = [] #creates a list of every position for every step
    mm_per_step = float(mystepper.screw_pitch)/mystepper.steps_per_rev #calculates the distance the stage moves for each step
    for i in range (1, num_steps):
        position_list.append(i*mm_per_step)#converts steps to mm, so the math is based on mm not steps
    return position_list

#Creates a vector that holds all the delay values for the stepper motor speed. Delay is the inverse of pulse frequency
def create_delay_vector(velocity_vector,mystepper):
    delay_vector = []
    for i in range (len(velocity_vector)):
        delay_vector.append(calculate_delay(velocity_vector[i], mystepper)) #calculates the delay necessary for a lirear velocityy at that speed
    return delay_vector

    

#creates a list that holds all the potential velocity values when the linear stage is moving at constant velocity
#uses the equation v = ax+b (x is in mm and it is from the position list created in a different function)
def create_linear_velocity_vector(const_a, const_b, position_list):
    velocity_list = []
    for i in range (len(position_list)):
        v=const_a * position_list[i] + const_b
        velocity_list.append(v)
    return velocity_list      


#creates a list that holds all the potential velocity values when the linear stage is moving at constant velocity
#uses the equation v = ax^2+bx+c (x is in mm and it is from the position list created in a different function)
def create_constant_jerk_vector(const_a, const_b, const_c, position_list):
    velocity_list = []
    for i in range (len(position_list)):
        v = const_a*((position_list[i])**2) + const_b*position_list[i]+ const_c
        velocity_list.append(v)
    return velocity_list



#These three functions serve the same purpose. They are the driver functions that actually allow the motor to move at 
# no acceleration, constant acceleration and linear acceleration
#First a vector is created that holds the linea stage's position in regards to home at each step.
#Second a list is created that stores the velocity at each of these psitions. This step is skipped when there is no acceleration since velocity is constant
#Then each velocity is converted into a delay so the stepper motor knows how long it should wait for it to turn at a certain velocity
#Finally the motor runs at a speed depsngin on the value found in the delay list

def run_motor_no_acceleration(initial_position, final_position, mystepper, const_a):
    position_list =create_Yc_vector(initial_position, final_position, mystepper)
    const_delay = calculate_delay(const_a, mystepper)
    for i in range (len(position_list)):
        runmotor(mystepper, const_delay, ETCHANT_DIRECTION)
def run_motor_constant_acceleration(initial_position, final_position, const_a, const_b, mystepper):
    position_vector = create_Yc_vector(initial_position, final_position, mystepper)
    velocity_vector = create_linear_velocity_vector(const_a, const_b, position_vector)
    del_vector = create_delay_vector(velocity_vector, mystepper)
    for i in range(len(del_vector)):
        runmotor(mystepper, del_vector[i], ETCHANT_DIRECTION)   
def run_motor_linear_acceleration(inital_position, final_position, const_a, const_b, const_c, mystepper):
    position_vector = create_Yc_vector(inital_position,final_position,mystepper)
    vel_vector = create_constant_jerk_vector(const_a, const_b,const_c, position_vector)
    del_vector = create_delay_vector(vel_vector,mystepper)
    for i in range(len(del_vector)):
        runmotor(mystepper, del_vector[i], ETCHANT_DIRECTION)






    
        

            
        

        

        
    
    
        
        
        
        
        
        
        
