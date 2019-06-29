#This program was created by Vishwa Nathan (vnathan@umich.edu) on June 28, 2019


#THIS FILE CONTAINS THE HELPER FUNCTIONS WHICH ARE USED TO CONTROL THE VELOCITY OF THE LINEAR STAGE


from time import sleep #imports sleep function used by the run_motor command
import RPi.GPIO as GPIO #allows for use of GPIO pins
GPIO.setwarnings(False) #Turns off unnecessary warnings provided by Raspberry Pi

GPIO.setmode(GPIO.BCM) #uses BCM mode for pin layout (Don't change)


#STEPPER MOTOR CLASS

#Creates a stepper motor class. This class takes in the step_angle, leadscrew pitch, pulse pin, direction pin and the number of microsteps in one full step. 

class stepper:
    def __init__(self, step_angle, screw_pitch, pulse_pin, dir_pin, msteps):
        self.screw_pitch = float(screw_pitch)
        self.pulse_pin = int(pulse_pin)
        self.dir_pin = int(dir_pin)
        self.steps_per_rev = int((360/step_angle)*msteps)
        GPIO.setup(int(pulse_pin), GPIO.OUT) #initializes the pulse pin as an output
        GPIO.setup(int(dir_pin), GPIO.OUT) #initializes the direction pin as an output



#Helper function to calculate overall change in position from the start point to the final point
def delta_position(final_position, initial_position):
    return (abs(final_position-initial_position)) #As a result, only the change in position matters, not its initial and final position.

#Returns the number of motor rotations required to move the stage a specified distance
def calculate_rotations(mystepper, initial_position, final_position):
    delta_pos = delta_position(final_position,initial_position) #calculates the distance the stage moves
    num_rotations = delta_pos/(mystepper.screw_pitch) #divides the ttravel distance by the screw pitch to calculate the number of rotations
    return num_rotations


#Creates a list of the linear stage's position at each step. This function calculates the number of steps required to travel a specified distance 
#and stores each step in a list. Each step is then converted to mm. The values stored in the list are its position at each step, not how far it moves with one step.
#Example: The linear stage is set to move 10 mm and it moves at 2mm/step. The values in the position list will be [0,2,4,6,8,10] not [2,2,2,2,2]
def create_Yc_vector(initial_position, final_position, mystepper):
    total_rotations = calculate_rotations(mystepper, initial_position, final_position) #calculates rotations
    num_steps = int(total_rotations * mystepper.steps_per_rev) #calculates number of total steps by multiplying the number of rotations by steps per rotation
    position_list = [] #creates a list variable to store every position for every step
    mm_per_step = float(mystepper.screw_pitch)/mystepper.steps_per_rev #calculates the distance the stage moves for each step
    for i in range (1, num_steps):
        position_list.append(i*mm_per_step)#converts steps to mm and appends it to the list.
    return position_list

#Creates a list which holds the stage's velocity at each step. This function is used regardless of the velocity profile
def create_velocity_vector(const_a, const_b , const_c , position_list):
        velocity_list = [] 
        for i in range (len(position_list)):
                v = float(const_c)*(position_list[i]**2)+ float(const_b)*position_list[i]+float(const_a) #calculates velocity based on the equation ct^2+bt+a
                velocity_list.append(v) #appends the velocity to the list.
        return velocity_list

#Calculates the delay which in turn controls the speed of the motor.
#Based on this equation
        #Linear velocity = (screw pitch * pulse_frequency)/ (steps per revolution of stepper motor)
#Rearranged to solve for pulse_frequency
#delay = 1/pulse frequency (From the equation (seconds = 1/frequency))
def calculate_delay(linear_velocity, mystepper):
    numerator = linear_velocity * mystepper.steps_per_rev 
    denominator = mystepper.screw_pitch
    pulse_freq = numerator/denominator
    delay = 1.0/pulse_freq
    return delay

#Creates a list that holds all the delay values for the stepper motor speed. Delay is the inverse of pulse frequency
def create_delay_vector(velocity_vector,mystepper):
    delay_vector = []
    for i in range (len(velocity_vector)):
        delay_vector.append(calculate_delay(velocity_vector[i], mystepper)) #calculates the delay necessary for the motor to travel at a specified velocity
    return delay_vector

#Moves the motor one step
def runmotor(mystepper, delay, direction):
    GPIO.output(mystepper.dir_pin, direction) #sets direction of motor
    GPIO.output(mystepper.pulse_pin,1) #sends a pulse to the motor to move one step
    sleep(delay) 
    GPIO.output(mystepper.pulse_pin,0) #turns off the motor
    sleep(delay)

#This function utilizes the previous functions to move the stage
def move_linear_stage(initial_position, final_position, mystepper, const_a, const_b, const_c, direction):
        position_vector = create_Yc_vector(float(initial_position), float(final_position), mystepper) #creates a list of the stage's position for each step
        vel_vector = create_velocity_vector(float(const_a), float(const_b), float(const_c), position_vector) #calculates the stage's velocity at each step
        del_vector = create_delay_vector(vel_vector,mystepper) #converts the velocity list into delays
        for i in range(len(del_vector)): 
                runmotor(mystepper, del_vector[i], direction) 


#Alternate move function which is used in the home function. It does not calculate velocity at each step since the home function moves at a constant velocity.
def movedistance(mystepper, delay, direction, distance):
    for x in range (0, distance):
        runmotor(mystepper, delay, direction)


# Homes the linear stage towards the endstop and then moves it four full revolutions away from the endstop to prevent retriggering. 
# Only used if the stage has an endstop
def home(mystepper, limitswitch_pin, home_speed, direction):
    while(GPIO.input(limitswitch_pin)==True): #run the motor while the endstop is not pressed
        runmotor(mystepper, home_speed, direction)
    GPIO.output(mystepper.pulse_pin, 0) 
    if (direction ==1): #Changes the direction
        direction =0
    else:
        direction =1
    
    movedistance(mystepper, home_speed*2, direction, 4*mystepper.steps_per_rev) #to move away from the endstoop








    



    
        

            
        

        

        
    
    
        
        
        
        
        
        
        
