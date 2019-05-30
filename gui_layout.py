
#This file contains all of the information for the layout of the GUI


from tkinter import *
from tkinter import messagebox


#Sets up main window for Tkinter
master = Tk()




#All of these give labels for the motor information
Label(master, text = "Motor Information", font = ('Montserrat', 28)). grid(row =0, column = 3, sticky="news")

Label(master).grid(row =1)
Label(master, text = "Step Angle", font = ('Montserrat', 22)).grid(row=2, column =1)
Label(master, text="Screw Pitch (mm)", font = ('Montserrat', 22)).grid(row=2, column =2)
Label(master, text="Steps per Revolution", font = ('Montserrat', 22)).grid(row=2, column =3)
Label(master, text="Pulse Pin", font = ('Montserrat', 22)).grid(row=2, column =4)
Label(master, text="Direction Pin", font = ('Montserrat', 22)).grid(row=2 ,column =5)


#These create the entry boxes for the motor informatiom
SA_e = Entry(master) #step angle
SP_e = Entry(master) #Screw pitch
SPR_e = Entry(master) #steps per revolution
PP_e = Entry(master) #pulse pin
DP_e = Entry(master) # direction pin


#lays out the location of the entry boxes for the motor information
SA_e.grid(row=3, column=1)
SP_e.grid(row=3, column=2)
SPR_e.grid(row=3, column=3)
PP_e.grid(row=3, column=4)
DP_e.grid(row=3, column=5)




#Sets up the labels for all the constants
Label(master).grid(row =4)
Label(master).grid(row =5)
Label(master, text =  "Constants", font = ('Montserrat', 28)).grid(row =6, column = 3)
Label(master).grid(row = 7)
Label(master, text =  "a (mm/sec)", font = ('Montserrat', 22)).grid(row =8, column = 2)
Label(master, text =  "b (1/sec)", font = ('Montserrat', 22)).grid(row =8, column = 3)
Label(master, text =  "c", font = ('Montserrat', 22)).grid(row =8, column = 4)


#creates entry boxes for all the constants and gives the location of these boxes
a_e= Entry(master)
b_e = Entry(master)
c_e = Entry(master)


a_e.grid(row = 9, column =2)
b_e.grid(row=9, column = 3)
c_e.grid(row =9, column=4)



#Depth Information
Label(master).grid(row =10)
Label(master).grid(row =11)
Label(master, text = "Channel Length", font = ('Montserrat', 28) ).grid(row =12, column=3)
Label(master).grid(row =13)
Label(master, text =  "Etch Rate", font = ('Montserrat', 22)).grid(row =14, column = 2)
Label(master, text = "Initial Position", font = ('Montserrat', 22) ).grid(row =14, column=3)
Label(master, text = "Final Position", font = ('Montserrat', 22) ).grid(row =14, column=4)



i_p = Entry(master) #initial position
i_p.grid(row = 15, column = 3)
f_p=Entry(master) #final position
f_p.grid(row=15, column =4)
e_r = Entry(master) #etch rate
e_r.grid(row=15, column=2)


# gives location and such for each of the buttons
Label(master).grid(row =16)
Label(master).grid(row =17)
rcv=Button(master, text="Run Constant Velocity", relief = RAISED)
rcv.grid(row =18, column =2)
rca=Button(master, text="Run Constant Acceleration")
rca.grid(row =18, column =3)
rcj=Button(master, text="Run Constant Jerk")
rcj.grid(row =18, column =4)

Label(master).grid(row=19)
Label(master).grid(row=20)



#import photos

up_arrow= PhotoImage(file = "green-arrow.png")
up_arrow = up_arrow.subsample(2,2)

up_arrow_flip = PhotoImage(file = "up_arrow_flip.png")
up_arrow_flip = up_arrow_flip.subsample(2,2)

#set up homing and direction buttons


home_button = Button(master, text = "Home" )
home_button.grid(row =3, column = 8)
move_ten = Button(master, text = "10mm", image = up_arrow, compound = LEFT )
move_ten.grid(row = 8, column = 8)
move_one= Button(master, text = "1mm", image = up_arrow, compound = LEFT)
move_one.grid(row = 9, column =8)
move_neg_one= Button(master, text = "1mm", image = up_arrow_flip, compound = LEFT)
move_neg_one.grid(row = 10, column = 8)
move_neg_ten = Button(master, text ="10mm", image = up_arrow_flip, compound = LEFT) 
move_neg_ten.grid(row =11, column =8)





#allows the window to be resized at will
master.grid_columnconfigure(0, weight =1)
master.grid_columnconfigure(1, weight =1)
master.grid_columnconfigure(2, weight =1)
master.grid_columnconfigure(3, weight =1)
master.grid_columnconfigure(4, weight =1)
master.grid_columnconfigure(5, weight =1)
master.grid_columnconfigure(6, weight =1)
master.grid_columnconfigure(7, weight =1)
master.grid_columnconfigure(8, weight =1)
master.grid_columnconfigure(8, weight =1)
master.grid_columnconfigure(9, weight =1)



master.grid_rowconfigure(0, weight =1)
master.grid_rowconfigure(1, weight =1)
master.grid_rowconfigure(2, weight =1)
master.grid_rowconfigure(3, weight =1)
master.grid_rowconfigure(4, weight =1)
master.grid_rowconfigure(5, weight =1)
master.grid_rowconfigure(6, weight =1)
master.grid_rowconfigure(7, weight =1)
master.grid_rowconfigure(8, weight =1)
master.grid_rowconfigure(9, weight =1)
master.grid_rowconfigure(10, weight =1)
master.grid_rowconfigure(11, weight =1)
master.grid_rowconfigure(12, weight =1)
master.grid_rowconfigure(13, weight =1)
master.grid_rowconfigure(14, weight =1)
master.grid_rowconfigure(15, weight =1)
master.grid_rowconfigure(16, weight =1)
master.grid_rowconfigure(17, weight =1)
master.grid_rowconfigure(18, weight =1)

mainloop()






