#####
#mortgageCalc.py
# 
# PLTW training
# version 7/14/2016
# Phil Cazella & Craig Hoiska
####

import Tkinter
from Tkinter import *

#####
# Create root window 
####
root = Tkinter.Tk()

# Make and place a canvas widget for events and drawing
canvas = Canvas(root, height=600, width=400, relief=RAISED, bg='white')
canvas.grid() #Puts the canvas in the main Tk window

# Instantiate and place slider
radius_slider = Tkinter.Scale(root, from_=1, to=150, label='Years')
radius_slider.grid(row=6, column=0, sticky=Tkinter.W)
# Create and place directions for the user
text = Tkinter.Label(root, text='Drag slider \nto adjust\nterm(years).')
text.grid(row=5, column=0)

root.mainloop()