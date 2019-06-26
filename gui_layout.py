import tkinter as tk
from tkinter import ttk, font, messagebox
# from PIL import ImageTk, Image





class resizeable_window:
    def __init__(self, parent):
        self.parent = parent
        self.parent.configure(background = '#CECECE') #00274c, D0D0D0 FFCB05
        self.parent.geometry("1080x750")
        self.parent.title("Microfluidic Etch Program")


 

        #Setting up row and column configuration for the parent window
        for x in range (0, 9, 4):
            self.parent.columnconfigure(x, {'minsize': 48})
        for x in range(1, 4):
            self.parent.columnconfigure(x, {'minsize': 96})
        for x in range(5, 9):
            self.parent.columnconfigure(x, {'minsize': 96})
        self.parent.rowconfigure(0, {'minsize':55})
        self.parent.rowconfigure(1, {'minsize': 443})
        self.parent.rowconfigure(2, {'minsize': 222})
        #Two frames for the two sides
        self.f1 =tk.Frame(self.parent, background = "White")
        self.f2 = tk.Frame(self.parent, background = "#CECECE") 
        self.f1.grid(row =1,column =1, columnspan =4)
        self.f2.grid(row =1,column =5, columnspan =3)


        #setting up row and column configuration for frame 1
        for x in range (0,7):
            self.f1.rowconfigure(x, {'minsize': 44})
        self.f1.rowconfigure(7, {'minsize': 88})
        for x in range(0,8):
            self.f2.rowconfigure(x, {'minsize': 60})





        #adding logo
               

        logo = tk.PhotoImage(file ="group_logo_text.png")
        logo_label = tk.Label(self.parent, image = logo, bg = '#CECECE' )
        logo_label.image = logo
        logo_label.grid(row =2, column =6)

        #Adding widgets for frame 1
        etch_program_label = tk.Label(self.f1, text = "Etch Program", font = ('Avenir 24 bold'), fg = 'black', bg = 'white' )
        etch_program_label.grid(row =0, columnspan =3)
        #Label for the speed equatin
        speed_label = tk.Label(self.f1, text = "Speed = " + u'ct\u00B2'+ " + bt + a ", font = ('Avenir 18 italic'), bg = "white")
        speed_label.grid(row =1, columnspan=3, )



        #Creates labels, and entry boxes. The frame is used to add a border to the entry box
        fin_pos_label=tk.Label(self.f1)
        init_pos_label =tk.Label(self.f1)
        a_label =tk.Label(self.f1)
        b_label =tk.Label(self.f1)
        c_label =tk.Label(self.f1)
       
        fin_pos_entryframe = tk.Frame(self.f1)
        init_pos_entryframe = tk.Frame(self.f1)
        a_entryframe = tk.Frame(self.f1)
        b_entryframe = tk.Frame(self.f1)
        c_entryframe = tk.Frame(self.f1)
        
        self.fin_pos_entry = tk.Entry(fin_pos_entryframe)
        self.init_pos_entry= tk.Entry(init_pos_entryframe)
        self.a_entry = tk.Entry(a_entryframe)
        self.b_entry = tk. Entry(b_entryframe)
        self.c_entry = tk.Entry(c_entryframe)


        label_list = [init_pos_label, fin_pos_label, a_label, b_label, c_label]
        entry_list = [self.init_pos_entry, self.fin_pos_entry, self.a_entry, self.b_entry, self.c_entry]
        entryframe_list = [ fin_pos_entryframe, init_pos_entryframe, a_entryframe, b_entryframe, c_entryframe]
        labeltext_list = ["Initial Position", "Final Position", "A [mm/s]", "B [mm/s" + u'\u00B2'+ "]", "C [mm/s" + u'\u00B3'+ "]"]
       
        def position_and_config_widget(label, borderframe, entrybox, labeltext, row, column, bg_color):
            label.config(text = labeltext, font = ('Avenir 18'), bg = bg_color)
            label.grid(row=row, column = column, sticky = tk.W, padx =20)
            borderframe.config(bg = "Black", borderwidth =1)
            borderframe.grid(row = row, column = column +1, columnspan =2,sticky = tk.E, padx =20)
            entrybox.config(relief="flat", highlightthickness=0)
            entrybox.grid(row =0, column =0)


        for x in range (0, 5):
            position_and_config_widget(label_list[x], entryframe_list[x], entry_list[x], labeltext_list[x], (x+2), 0, "white")

        


        
        constant_vel_pic = tk.PhotoImage(file = "constant_vel.gif")
        linear_vel_pic = tk.PhotoImage(file = "linear_vel.gif")
        non_linear_vel_pic = tk.PhotoImage(file = "non_linear_vel.gif")
        constant_vel_label = tk.Label(self.f1, image = constant_vel_pic, bg = "white")
        linear_vel_label = tk.Label(self.f1, image = linear_vel_pic, bg = "white")
        non_linear_vel_label = tk.Label(self.f1, image = non_linear_vel_pic, bg = "white")

        self.constant_vel_button = tk.Button(self.f1, text = "Run" )
        self.linear_vel_button = tk.Button(self.f1, text = "Run")
        self.non_linear_vel_button = tk.Button(self.f1, text = "Run")

        image_list = [constant_vel_pic, linear_vel_pic, non_linear_vel_pic]
        image_label_list = [constant_vel_label, linear_vel_label, non_linear_vel_label]
        image_button_list = [self.constant_vel_button, self.linear_vel_button, self.non_linear_vel_button]
        for x in range(0,3):
            image_label_list[x].image= image_list[x]
            if (x ==0):
                image_label_list[x].grid(row =7, column =x, sticky = tk.W , pady = (30, 8), padx =(20,0))  
                image_button_list[x].grid(row =8, column =x, sticky = tk.W +tk.E, padx = (20, 85), pady=(0,20) ) 
            elif (x==1):
                image_label_list[x].grid(row =7, column =x, sticky = tk.W , pady = (30,8), padx =(10,10))
                image_button_list[x].grid(row =8, column =x, sticky = tk.W +tk.E, padx = (10,10), pady=(0,20) )
            else: 
                image_label_list[x].grid(row =7, column =x, sticky =  tk.W, pady = (30,8), padx = (30,20))
                image_button_list[x].grid(row =8, column =x, sticky = tk.W +tk.E, padx = (35,20), pady=(0,20) )


        movement_speed_label = tk.Label(self.f2, background = '#CECECE')
        movement_speed_entryframe = tk.Frame(self.f2)
        # speed_label.grid(row =0, column =0)
        self.movement_speed_entry_box = tk.Entry(movement_speed_entryframe)
        # speed_entry_box.grid(row =0, column =1)
        
        position_and_config_widget(movement_speed_label, movement_speed_entryframe, self.movement_speed_entry_box, "Speed (mm/s)", 0,0, "#CECECE")

        tentop = tk.PhotoImage(file = "ten_top.png")
        self.pos_ten_button = tk.Label(self.f2, text = "10", image = tentop)
        self.pos_ten_button.image = tentop

        onetop = tk.PhotoImage(file = "one_top.png")
        self.pos_one_button = tk.Label(self.f2, text = "1", image = onetop)
        self.pos_one_button.image = onetop
       
        tenthtop = tk.PhotoImage(file = "tenth_top.png")
        self.pos_tenth_button = tk.Label(self.f2, text = "0.1", image = tenthtop)
        self.pos_tenth_button.image = tenthtop


        home_image = tk.PhotoImage(file ="homebutton.png")
        self.home_button = tk.Label(self.f2, text = "Home", image = home_image)
        self.home_button.image=home_image

        tenthbottom = tk.PhotoImage(file = "tenth_bottom.png")
        self.neg_tenth_button = tk.Label(self.f2, text = "-10", image = tenthbottom)
        self.neg_tenth_button.image = tenthbottom

        onebottom = tk.PhotoImage(file = "one_bottom.png")
        self.neg_one_button = tk.Label(self.f2, text = "-1", image = onebottom)
        self.neg_one_button.image = onebottom

        tenbottom = tk.PhotoImage(file = "ten_bottom.png")
        self.neg_ten_button = tk.Label(self.f2, text = "-0.1", image = tenbottom)
        self.neg_ten_button.image  = tenbottom

        button_list = [self.pos_ten_button, self.pos_one_button, self.pos_tenth_button, self.home_button, self.neg_tenth_button, self.neg_one_button, self.neg_ten_button]

        for index, button in enumerate(button_list):
            button.config(background ='#CECECE')
            button.grid(row =index+1,  sticky =  tk.W+ tk.E, columnspan =3)










        # Use second frame to add a button for homing and ther such shenanigans
        # movement_canvas = tk.Canvas(self.f2, width = 247, height = 248, bg = "#00274C", relief = "flat")
        # movement_canvas.grid(row =0, column =0)
        # mainbutton_image = tk.PhotoImage(file ="printrun_button.png")
        # self.f2.mainbutton_image= mainbutton_image
        # canvas_image = movement_canvas.create_image(0,0, image = mainbutton_image, anchor = "nw")
        # test_label = tk.Label(self.f2, text = "potato")
        # test_label.grid(row =1, column =0)

        # movement_canvas.bind("<Button-1>", lambda event:print_coordinates(event, test_label))



        


        

        # other_label = tk.Label(self.f2, text = "Constant Speed Movement", font = ('Avenir 24 bold'))
        # other_label.grid(row =0, column =0)
        





root = tk.Tk()
root.resizable(0,0)
# for names in sorted(tk.font.families()):
#     print(names)
#print(u'  change = (ct\u00B2)')
mw = resizeable_window(root)
tk.mainloop()


