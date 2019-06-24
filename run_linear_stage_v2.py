from gui_layout_v2 import *
from linear_stage_functions import *
import motor_constants 


#constructs the stepper mottor  class that wll be used. All oft these valuees can be found/changed in the file motor_constants.py. 
#The constructor for the motor can be found in linear_stage_functions.py
STAGE_MOTOR = stepper(STEP_ANGLE, SCREW_PITCH, PULSE_PIN, DIR_PIN, MICROSTEPS_PER_STEP)


#This is the program which will be bound to the button to allow the linear stage to move at different linear velocity profiles
def run_etch_program(initial_position, final_position, mystepper, const_a, const_b, const_c):
    global ETCHANT_DIRECTION
    global HOME_DIRECTION
    global ENDSTOP_ENABLED
    global HOMING_SPEED
   # velocity profile is a functor that will be replaced by a value when bound to an actual button
    move_linear_stage(initial_position, final_position, mystepper, a, b, c, ETCHANT_DIRECTION)
    if(ENDSTOP_ENABLED==True):
        home(mymotor, LIMITSWITCH)
    else:
        homing_velocity = mystepper.screw_pitch/(HOMING_SPEED*mystepper.steps_per_rev)
        move_linear_stage(initial_position, final_position+50, mystepper, homing_velocity, 0, 0, HOME_DIRECTION)


#This function will home the linear stage if an endstop is present
def run_home():
    try:
        global ENDSTOP_ENABLED
        if (ENDSTOP_ENABLED==True):
            initiate_motor()
            home(mymotor, limitswitch)



constant_vel_button.config(command = lambda: run_etch_program(init_pos_entry.get(), fin_pos_entry.get(), STAGE_MOTOR, a_entry.get(), 0,0))
linear_vel_button.config (command = lambda:run_etch_program(init_pos_entry.get(), fin_pos_entry.get(), STAGE_MOTOR, a_entry.get(), b_entry.get(),0))
non_constant_vel_button.config(command = lambda:run_etch_program(init_pos_entry.get(), fin_pos_entry.get(), STAGE_MOTOR, a_entry.get(), b_entry.get(),c_entry.get()))