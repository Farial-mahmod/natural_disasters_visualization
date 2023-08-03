import os
from tkinter import *

"""
Module / Library        Use          

tkinter                 library used to produce interactive Graphical User Interface (GUI)
os                      built-in module to perform any Operating System level operation
"""


tk = Tk()                                                 # preparing a Tkinter instance
tk.title('Data Visualization of Natural Disasters')       # adding Title
tk.geometry("325x195")                                    # window-size


def pandemic():
    # function to view pandemic data
    os.system('python3 pandemics.py')

def earthquake():
    # function to view earthquake data
    os.system('python3 earthquakes.py')

def flood():
    # function to view flood data
    os.system('python3 floods.py')

def famine():
    # function to view famine data
    os.system('python3 famines.py')



# Buttons to call each function

pan_btn = Button(tk,text="Pandemics", command = pandemic, pady=5, width=8, bg="#efe469")
ear_btn = Button(tk,text="Earthquakes", command = earthquake, pady=5, width=8, bg="grey")
flo_btn = Button(tk,text="Floods", command = flood, pady=5, width=8, bg="lightblue")
fam_btn = Button(tk,text="Famines", command = famine, pady=5, width=8, bg="brown")


# positioning the buttons

flo_btn.pack(side = RIGHT)
fam_btn.pack(side = LEFT)
pan_btn.pack(side = TOP)
ear_btn.pack(side = BOTTOM)

# running the mainloop
tk.mainloop()
