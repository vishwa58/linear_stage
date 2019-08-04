#This program was created by Vishwa Nathan (vnathan@umich.edu) on June 28, 2019


#THIS FILE CONTAINS THHE COMMANDS THAT ALLOW THE BUTTONS ON THE GUI TO WORK

from gui_layout import *
from linear_stage_functions import *
from motor_constants import *


#constructs the stepper motor class that will be used. All of these values can be found/changed in the file motor_constants.py. 
#The constructor for the motor can be found in linear_stage_functions.py
STAGE_MOTOR = stepper(STEP_ANGLE, SCREW_PITCH, PULSE_PIN, DIR_PIN, MICROSTEPS_PER_STEP)


#This is the program which will be bound to the button to allow the linear stage to move at different linear velocity profiles
def run_etch_program(initial_position, final_position, mystepper, const_a, const_b, const_c):
    global ETCHANT_DIRECTION
    global HOME_DIRECTION
    global ENDSTOP_ENABLED
    global HOMING_SPEED
    #See linear_stage_functions for more information on the following function
    move_linear_stage(float(initial_position), float(final_position), mystepper, float(const_a), float(const_b), float(const_c), ETCHANT_DIRECTION)
    
    #re-comment the following code if you would like to utilize homing
    # if(ENDSTOP_ENABLED==True):
    #     home(mystepper, LIMITSWITCH, HOMING_SPEED, HOME_DIRECTION)
    # else:
    #     homing_velocity = mystepper.screw_pitch/(HOMING_SPEED*mystepper.steps_per_rev)
    #     move_linear_stage(float(initial_position), float(final_position)+50, mystepper, float(homing_velocity), 0, 0, HOME_DIRECTION)


#This function will home the linear stage if an endstop is present
def run_home(mymotor, limitswitch, homingspeed, direction):
    global ENDSTOP_ENABLED
    
    if(ENDSTOP_ENABLED==True):
        home(mymotor, limitswitch, homingspeed, direction)
    else:
        print("set ENDSTOP_ENABLED to true if you would like to utilize homing")




# mw.constant_vel_button.config(command = lambda:run_etch_program(mw.init_pos_entry.get(), mw.fin_pos_entry.get(), STAGE_MOTOR, mw.a_entry.get(), 0,0))
# mw.linear_vel_button.config (command = lambda:run_etch_program(mw.init_pos_entry.get(), mw.fin_pos_entry.get(), STAGE_MOTOR, mw.a_entry.get(), mw.b_entry.get(),0))
# mw.non_linear_vel_button.config(command = lambda:run_etch_program(mw.init_pos_entry.get(), mw.fin_pos_entry.get(), STAGE_MOTOR, mw.a_entry.get(), mw.b_entry.get(),mw.c_entry.get()))

mw.constant_vel_label.bind("<Button-1>", lambda x :run_etch_program(mw.init_pos_entry.get(), mw.fin_pos_entry.get(), STAGE_MOTOR, mw.a_entry.get(), 0,0))
mw.linear_vel_label.bind ("<Button-1>", lambda x :run_etch_program(mw.init_pos_entry.get(), mw.fin_pos_entry.get(), STAGE_MOTOR, mw.a_entry.get(), mw.b_entry.get(),0))
mw.non_linear_vel_label.bind ("<Button-1>", lambda x :run_etch_program(mw.init_pos_entry.get(), mw.fin_pos_entry.get(), STAGE_MOTOR, mw.a_entry.get(), mw.b_entry.get(),mw.c_entry.get()))

mw.pos_ten_button.bind("<Button-1>",  lambda a: move_linear_stage(10, 0, STAGE_MOTOR, mw.movement_speed_entry_box.get(), 0, 0, HOME_DIRECTION))
mw.pos_one_button.bind("<Button-1>",  lambda a: move_linear_stage(1, 0, STAGE_MOTOR, mw.movement_speed_entry_box.get(), 0, 0, HOME_DIRECTION))
mw.pos_tenth_button.bind("<Button-1>",  lambda a: move_linear_stage(0.1, 0, STAGE_MOTOR,mw.movement_speed_entry_box.get(), 0, 0, HOME_DIRECTION))

mw.neg_ten_button.bind("<Button-1>",  lambda a: move_linear_stage(10, 0, STAGE_MOTOR, mw.movement_speed_entry_box.get(), 0, 0, ETCHANT_DIRECTION))
mw.neg_one_button.bind("<Button-1>",  lambda a: move_linear_stage(1, 0, STAGE_MOTOR, mw.movement_speed_entry_box.get(), 0, 0, ETCHANT_DIRECTION))
mw.neg_tenth_button.bind("<Button-1>",  lambda a: move_linear_stage(0.1, 0, STAGE_MOTOR, mw.movement_speed_entry_box.get(), 0, 0, ETCHANT_DIRECTION))

mw.home_button.bind("<Button-1>", lambda x: run_home(STAGE_MOTOR, LIMITSWITCH, HOMING_SPEED, HOME_DIRECTION))

tk.mainloop()