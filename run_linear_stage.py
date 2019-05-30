
#This is the driver program that allows the user to actually run the program

from gui_layout import *
from linear_stage_functions import *
limitswitch =21

mymotor = stepper(1,1,1,1,1)

ENDSTOP_ENABLED = False

HOMING_SPEED = .00001


#These represent the direction the motor will move. 
#If the stage is not moving in the correct direction either swap the stepper motor wires or swap these values.
# (Set HOME_DIRECTION to 1 and ETCHANT_DIRECTION to 0)
HOME_DIRECTION =0
ETCHANT_DIRECTION =1

def initiate_motor():
    try:
        global mymotor
        newmotor = stepper(SA_e.get(), SP_e.get(), PP_e.get(), DP_e.get(),SPR_e.get())
        mymotor = newmotor
    except:
        messagebox.showerror("Error", "The Motor information you have entered is invalid. Please try again")
        #print("The Motor information you have entered is invalid. Please try again")

def testglobal():
    messagebox.showinfo("INFORMATION",mymotor.step_angle)

    #print(mymotor.step_angle)
def run_constant_velocity():
    try:
        global ETCHANT_DIRECTION
        global ENDSTOP_ENABLED
        global HOMING_SPEED
        initiate_motor()
        const_velocity_movement(float(i_p.get()), float(f_p.get()), mymotor, float(a_e.get()), ETCHANT_DIRECTION)
        if(ENDSTOP_ENABLED==True):
            home(mymotor, limitswitch)
        else:
            const_velocity_movement(float(i_p.get()+50), float(f_p.get()), mymotor, float(HOMING_SPEED), HOME_DIRECTION)
    except:
        messagebox.showerror("Error", "Error has ocurred, please try again")
def run_constant_acceleration():
    try:
        global ETCHANT_DIRECTION
        global ENDSTOP_ENABLED
        global HOMING_SPEED
        initiate_motor()
        run_motor_linear_velocity(float(i_p.get()), float(f_p.get()), float(a_e.get()), float(b_e.get()), mymotor, ETCHANT_DIRECTION)
        if(ENDSTOP_ENABLED==True):
            home(mymotor, limitswitch)
        else:
            const_velocity_movement(float(i_p.get()+50), float(f_p.get()), mymotor, float(HOMING_SPEED), HOME_DIRECTION)
        
    except:
        messagebox.showerror("Error", "Error has ocurred, please try again")
def run_constant_jerk():
    try:
        global ETCHANT_DIRECTION
        global ENDSTOP_ENABLED
        global HOMING_SPEED
        initiate_motor()
        run_motor_non_linear_velocity(float(i_p.get()), float(f_p.get()), float(a_e.get()), float(b_e.get()),  float(c_e.get()), mymotor, ETCHANT_DIRECTION)
        
        if(ENDSTOP_ENABLED==True):
            home(mymotor, limitswitch)
        else:
            const_velocity_movement(float(i_p.get()+50), float(f_p.get()), mymotor, float(HOMING_SPEED), HOME_DIRECTION)
            
    except:
        messagebox.showerror("Error", "Error has ocurred, please try again")
def run_home():
    try:
        initiate_motor()
        home(mymotor, limitswitch)
        
    except:
        messagebox.showinfo("Error", "Unable to home linear stage")

def move_pos_ten():
    initiate_motor()
    movedistance(mymotor, .0003, 0, int((float(mymotor.steps_per_rev)/mymotor.screw_pitch * 10)))
def move_pos_one():
    initiate_motor()
    movedistance(mymotor, .0003, 0, int((float(mymotor.steps_per_rev)/mymotor.screw_pitch * 1)))
def run_neg_ten():
    initiate_motor()
    movedistance(mymotor, .0003, 1, int((float(mymotor.steps_per_rev)/mymotor.screw_pitch * 10)))
def run_neg_one():
    initiate_motor()
    movedistance(mymotor, .0003, 1, int((float(mymotor.steps_per_rev)/mymotor.screw_pitch * 1)))
    
    
        
    

rcv.config(command = run_constant_velocity)
rca.config(command = run_constant_acceleration)
rcj.config(command = run_constant_jerk)
home_button.config(command = run_home)
move_ten.config(command = move_pos_ten)
move_one.config(command = move_pos_one)
move_neg_ten.config(command = run_neg_ten)
move_neg_one.config(command = run_neg_one)





mainloop()