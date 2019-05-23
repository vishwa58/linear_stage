

from __future__ import print_function
from linear_stage_functions import *
import time
#import matplotlib.pyplot #as plt

#from time import sleep #imports sleep function
#import RPi.GPIO as GPIO #allows for use of GPIO pins

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
newstepper = stepper(1.8, 6, 24, 23, 1600)



#test _position vector creation
#newlist = create_Yc_vector(900, 1200, newstepper)
#
#print (len(newlist))
#for i in range(len(newlist)):
#    print(newlist[i], sep ='/n')


#test to recreate the data found in the velocity profiles from the excel sheet
#position_list = []
#for i in range (0,51):
#    position_list.append(i)
#a = 1
#b = .01
#R = .01
#
#vel_vector = create_linear_velocity_vector(a,b, position_list)
#
#for i in range (len(vel_vector)):
#    print(vel_vector[i], sep = '/n')
#    
#etch_height_vector = create_etch_height_vector(position_list, R, a, b)
#
#for i in range (len(etch_height_vector)):
#    print(etch_height_vector[i], sep = '/n')
#    


    
run_motor_linear_velocity(900, 1200, 1.66667, 0.0166667, newstepper)
#for x in range (0,1600):
#    runmotor(newstepper, .0003)
#for x in range (0,1600):
#    move_around(newstepper, .0004, 0)
#home(newstepper, 21)
    
#run_motor_linear_velocity(90, 120, .1, 0.01, 0.01, newstepper)
#print("thisd")
#
#pos_vector = create_Yc_vector(900,1200, newstepper)
#for i in range (len(pos_vector)):
#   print(pos_vector[i], sep = '/n')
#
#delay_vector = test_delay_vector(900, 1200, .0166667, 0.000166667, 0.000166667, newstepper)
#for i in range (len(delay_vector)):
#   print(delay_vector[i], sep = '/n')
#   
#delay_vector = test_delay_vector(900, 1200, 1.66667, 0.0166667, 0.0166667, newstepper)
#sum =0
#for i in range (1,400):
#   print(delay_vector[i], sep = '/n')
#   sum += delay_vector[i]
#print(sum)
#velocity_vector = create_linear_velocity_vector(.0166667, 0.000166667, pos_vector)
#for i in range (len(velocity_vector)):
#   print(velocity_vector[i], sep = '/n')


#this test creates some graphs to ensure that the linear velocity function works
#pos_vector=create_Yc_vector(900, 1200, newstepper)
#linear_velocity_vector = create_linear_velocity_vector(.0166667, .000166667, pos_vector)
#etch_height = create_etch_height_vector(pos_vector, .0001666667, .0166667, 0.000166667)
#
#plt.plot(pos_vector, linear_velocity_vector, 'r--')
#plt.savefig("graph.pdf")








