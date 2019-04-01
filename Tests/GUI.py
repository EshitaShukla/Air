'''
TestCase
'''


from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import*

from ttkthemes import themed_tk as tkt
from tkinter import Canvas
from tkinter.constants import *
from PIL import Image, ImageDraw, ImageTk
# import ttkthemes as ttk
# from ttkthemes import *

import time
import unittest
import pandas as pd
import dateutil
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

import os
import sys
import csv


root_dir_path = os.path.dirname(os.path.realpath(__file__))
Template_folder_address = p=str(os.path.join(root_dir_path, "Templates"))


bg3 = "snow"
fg4 = "grey"
fg3 = "grey"


from FlightProfile.src.Guidance.FlightPathFile import FlightPath

###########################

basestring = str

class Main(tkt.ThemedTk,tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tkt.ThemedTk.__init__(self)   ##
        self.get_themes()             ##
        self.set_theme("radiance")      ##
        #photo=PhotoImage(file=P)


        self.menu=Menu(self,background="red",foreground=bg3)
        self.config(menu=self.menu)

            ##
        self.submenu=Menu(self.menu,foreground="snow",background="red",activebackground="snow",activeforeground=fg3)
        self.menu.add_cascade(label="file",menu=self.submenu)


        a=self.submenu.add_command(label="developer info",command=lambda:self.show_frame(P01))
        b=self.submenu.add_command(label="contact us",command=lambda:self.show_frame(P02))

            ##
        self.submenu2=Menu(self.menu,foreground="snow",background="red",activebackground="snow",activeforeground=fg3)
        self.menu.add_cascade(label="Choose Theme",menu=self.submenu2)

        F1=tk.Frame(self)
        F1=tk.Frame(self,width=400,height=450)
        F1.place(height=7000, width=4000, x=100, y=100)
        F1.config()
        F1.pack(fill="both",expand=True)

        F1.grid_rowconfigure(0,weight=1)
        F1.grid_columnconfigure(0,weight=1)
        F1.config()

        self.frames={}

        for F in (P01, P02, P03):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.config(bg=bg3)
            frame.grid(row=0,column=0,sticky="nsew")



        self.show_frame(P01)

    def enter_show_frame(self,cont,event=None):
        frame=self.frames[cont]
        frame.tkraise()

    def show_frame(self,cont):

        frame=self.frames[cont]
        frame.config(bg=bg3)
        frame.tkraise()


class P01(tk.Frame):                     # Home Page

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        P = "C:\\Users\\Eshita Shukla\\Downloads\\workspace_new\\FlightProfile\\src\\Templates\\logo.png"
        photo = PhotoImage(file=P)
        label = Label(self,image =photo)
        label.image = photo # keep a reference!
        label.pack()


        x="""Developer Information"""
        label = Label(self,text=x,font="cmmi10 50",fg=fg3,bg=bg3)
        label.pack()

        y="""Developer: Eshita Shukla
Date of creation: September 24, 2017
Last modified: March 24, 2018

"""
        label = Label(self,text=y,font="cmmi 20",fg=fg3,bg=bg3)
        label.pack()

        b=ttk.Button(self,text="Let's begin!!!",command=lambda:controller.show_frame(P03))
        b.pack()

class P02(tk.Frame):                     # Home Page

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        x="""Contact Us"""
        label = Label(self,text=x,font="cmmi10 50",fg=fg3,bg=bg3)
        label.pack()

        y="""email: abcd@gmail.com
contact: @#$%^&*!^$

"""
        label = Label(self,text=y,font="cmmi 20",fg=fg3,bg=bg3)
        label.pack()

        b=ttk.Button(self,text="Let's begin!!!",command=lambda:controller.show_frame(P03))
        b.pack()

class P03(tk.Frame):                     # Home Page

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        root2 = self
        L1 = Label (root2, text = "Route: ")
        L1.grid(row = 2, column = 2)

        SRoute = StringVar()
        E1 = Entry (root2, textvariable = SRoute)
        E1.grid(row = 2, column = 4)

        L2 = Label (root2, text = "Code: ")
        L2.grid(row = 3, column = 2)

        Code = StringVar()
        E2 = Entry (root2, textvariable = Code)
        E2.grid(row = 3, column = 4)

        L3 = Label (root2, text = "Level: ")
        L3.grid(row = 4, column = 2)

        Level = StringVar()
        E3 = Entry (root2, textvariable = Level)
        E3.grid(row = 4, column = 4)

        L4 = Label (root2, text = "Cruise match: ")
        L4.grid(row = 5, column = 2)

        CMatch = StringVar()
        E4 = Entry (root2, textvariable = CMatch)
        E4.grid(row = 5, column = 4)


        L5 = Label (root2, text = "Mass: ")
        L5.grid(row = 6, column = 2)

        Mass = StringVar()
        E5 = Entry (root2, textvariable = Mass)
        E5.grid(row = 6, column = 4)

        # messagebox.showinfo("Title", "a Tk MessageBox")

        """
        strRoute = 'ADEP/CYMX/06-TAMKO-MATOR-DICEN-CHARLEVOIX-RIVIEREDULOUP-LOMSI-RESNO-NETKI-'
        strRoute += 'NIBOG-BELFAST-DUFFY-RINGA-SLYDA-ISLEOFMAN-KELLY-PENIL-ASNIP-MANCHESTER-'
        strRoute += 'DISAL-NAPEX-DOLAS-ENITO-DIBAL-BUKUT-LAMSO-EVELI-BASNO-PAMPUS-IVLUT-LUNIX-'
        strRoute += 'RENDI-EDUPO-NAPRO-DEPAD-AMOSU-MISGO-COLA-ROLIS-'
        strRoute += 'ADES/EDDF/25C'
        """
        def give_otp ():

            strRoute = E1.get()
            code = E2.get()
            level = int(E3.get())
            cruise_match = float(E4.get())
            mass = float(E5.get())

            flag = 0
            ErrorString = ""
            if level < 270:
                ErrorString += "level < 270\n"
                flag = 1
            elif level > 390:
                ErrorString += "level > 390\n"
                flag = 1

            if cruise_match < 0.78:
                ErrorString += "cruise_match < 0.78\n"
                flag = 1
            elif cruise_match > 0.86:
                ErrorString += "cruise_match > 0.86\n"
                flag = 1

            if mass < 50000:
                ErrorString += "mass < 50000\n"
                flag = 1
            elif mass > 230000:
                ErrorString += "level > 230000\n"
                flag = 1

            if flag == 1:
                messagebox.showerror("Error", ErrorString)
                SRoute = Code = Level = CMatch = Mass = 0
                return

            flightPath = FlightPath(route = strRoute,
                                    aircraftICAOcode = code,
                                    RequestedFlightLevel = level,
                                    cruiseMach = cruise_match,
                                    takeOffMassKilograms = mass)
            '''
            RFL:    FL 310 => 31000 feet
            Cruise Speed    Mach 0.78                                    
            Take Off Weight    62000 kgs    
            '''

            #strf_time =
            print ("=========== Flight Plan compute  =========== "+ time.strftime("%c"))
            L1 =Label (root2, text = "Flight Plan compute\t"+time.strftime("%c"))
            L1.grid()

            t0 = time.clock()
            print ('time zero= ' + str(t0))

            L2 =Label (root2, text = 'time zero= ' + str(t0))
            L2.grid(row = 10, columnspan = 2)

            lengthNauticalMiles = flightPath.computeLengthNauticalMiles()
            print ('flight path length= {0:.2f} nautics '.format(lengthNauticalMiles))

            L3 =Label (root2, text = 'flight path length= {0:.2f} nautics '.format(lengthNauticalMiles))
            L3.grid(row = 10, columnspan = 2)

            try:
                flightPath.computeFlight(deltaTimeSeconds = 1.0)
            except:
                print("flightPath")
            print ('simulation duration= ' + str(time.clock()-t0) + ' seconds')

            L4 =Label (root2, text = 'simulation duration= ' + str(time.clock()-t0) + ' seconds')
            L4.grid(row = 11, columnspan = 2)

            print ("=========== Flight Plan create output files  =========== " + time.strftime("%c"))
            try:
                flightPath.createFlightOutputFiles()
            except:
                print("Error Occured")

            L5 =Label (root2, text = "=========== Flight Plan create output files  =========== " + time.strftime("%c"))
            L5.grid(row = 12, columnspan = 2)

            print ("=========== Flight Plan end  =========== " + time.strftime("%c"))

            L6 =Label (root2, text = " Flight Plan end   " + time.strftime("%c"))
            L6.grid(row = 13, columnspan = 2)

        Submit = ttk.Button(root2, text = "Submit", command= lambda: give_otp())
        Submit.grid()




def hex2rgb(str_rgb):
    try:
        rgb = str_rgb[1:]

        if len(rgb) == 6:
            r, g, b = rgb[0:2], rgb[2:4], rgb[4:6]
        elif len(rgb) == 3:
            r, g, b = rgb[0] * 2, rgb[1] * 2, rgb[2] * 2
        else:
            raise ValueError()
    except:
        raise ValueError("Invalid value %r provided for rgb color."% str_rgb)

    return tuple(int(v, 16) for v in (r, g, b))

class GradientFrame(Canvas):

    def __init__(self, master, from_color, to_color, width=None, height=None, orient=HORIZONTAL, steps=None, fill=None, **kwargs):
        Canvas.__init__(self, master,**kwargs)
        if steps is None:
            if orient == HORIZONTAL:
                steps = height
            else:
                steps = width

        if isinstance(from_color, basestring):
            from_color = hex2rgb(from_color)

        if isinstance(to_color, basestring):
            to_color = hex2rgb(to_color)

        r,g,b = from_color
        dr = float(to_color[0] - r)/steps
        dg = float(to_color[1] - g)/steps
        db = float(to_color[2] - b)/steps

        if orient == HORIZONTAL:
            if height is None:
                raise ValueError("height can not be None")

            self.configure(height=height, bd=0, highlightthickness=0, relief='ridge')

            if width is not None:
                self.configure(width=width)

            img_height = height
            img_width = self.winfo_screenwidth()

            image = Image.new("RGB", (img_width, img_height), "#FFFFFF")
            draw = ImageDraw.Draw(image)

            for i in range(steps):
                r,g,b = r+dr, g+dg, b+db
                y0 = int(float(img_height * i)/steps)
                y1 = int(float(img_height * (i+1))/steps)

                draw.rectangle((0, y0, img_width, y1), fill=(int(r),int(g),int(b)))
        else:
            if width is None:
                raise ValueError("width can not be None")
            self.configure(width=width)

            if height is not None:
                self.configure(height=height)

            img_height = self.winfo_screenheight()
            img_width = width

            image = Image.new("RGB", (img_width, img_height), "#FFFFFF")
            draw = ImageDraw.Draw(image)

            for i in range(steps):
                r,g,b = r+dr, g+dg, b+db
                x0 = int(float(img_width * i)/steps)
                x1 = int(float(img_width * (i+1))/steps)

                draw.rectangle((x0, 0, x1, img_height), fill=(int(r),int(g),int(b)))

        self._gradient_photoimage = ImageTk.PhotoImage(image)

        self.create_image(0, 0, anchor=NW, image=self._gradient_photoimage)

############################


Meter2Feet = 3.2808 # one meter equals 3.28 feet
Meter2NauticalMiles = 0.000539956803 # One Meter = 0.0005 nautical miles
NauticalMiles2Meter = 1852 

class Test_Route(unittest.TestCase):


    def test_route(self):
    
    #sys.stdout = open('log.txt','w') #redirect all prints to this log file

        bg1 = "#ffffff"
        bg2 = "#ff0000"

        root=Main()
        root.get_themes()
        root.set_theme("radiance")
        fx=Frame(width=500,height=30, bd=0, highlightthickness=0, relief='ridge')
        fx.place(height=50, width=0, x=0, y=0)
        fx.pack(side="top",fill="both",expand=True)
        fx.grid_rowconfigure(1)
        fx.grid_columnconfigure(1)
        fx.config(bg="black")

        f1=Frame(width=500,height=30, bd=0, highlightthickness=0, relief='ridge', bg = "black")
        f1.place(height=50, width=0, x=0, y=0)
        f1.pack(side="bottom",fill="both",expand=True)
        f1.grid_rowconfigure(1)
        f1.grid_columnconfigure(1)
        f1.config(bg="black")

        f2=Frame(width=500,height=30, bd=0, highlightthickness=0, relief='ridge')
        f2.place(height=100, width=0, x=0, y=0)
        f2.pack(side="bottom",fill="both",expand=True)
        f2.grid_rowconfigure(1)
        f2.grid_columnconfigure(1)
        f2.config(bg="red")

        #self.x=GradientFrame(f, from_color=bg2, to_color=bg1, height=35,fill="both").pack(fill="both")
        self.y=GradientFrame(f2, from_color="#FFFfff", to_color=bg2, height=35,fill="both").pack(fill="both")
        self.z=GradientFrame(f1, from_color="#ff0000", to_color="#000000", height=35,fill="both").pack(fill="both")

        print ("=========== Flight Plan start  =========== " + time.strftime("%c"))

        root2 = fx

        def exit_function():
            # Put any cleanup here.
            sys.exit()
            root.destroy()

        root.protocol('WM_DELETE_WINDOW', exit_function)

        try:
            root.mainloop()
        except:
            pass

if __name__ == '__main__':

    unittest.main()

