#####
#mortgageCalc.py
# 
# PLTW training
# version 7/14/2016
# Phil Cazella & Craig Hoiska
####
import Mortgage
import Tkinter
from Tkinter import *


#####
#Controller
#####
DTO = Mortgage()

def UpdateView():
    #variable names are : rate, years, loan
    DTO.Principle = loan
    DTO.Rate = rate
    DTO.Term = years
    
    money_text.set(m.GetPayment())

#####
# Create root window 
####
root = Tkinter.Tk()
payment_text = Tkinter.Label(root, text='Monthly Payment:')
payment_text.grid(row=0, column=1)
mpayment_text = Tkinter.Label(root, text='$')
mpayment_text.grid(row=1, column=1)
money_text = Tkinter.Label(root, text='Amount to be borrowed:')
money_text.grid(row=1, column=0)
money = Entry(root)
money.grid(row=2,column=0)
# Instantiate and place Rate slider
rate_slider = Tkinter.Scale(root, from_=0, to=10, orient=HORIZONTAL, resolution=.5,length=300, label='Interest Rate')
rate_slider.grid(row=5, column=0, columnspan=2, sticky=Tkinter.W)
# Create and place directions for the user
rate_text = Tkinter.Label(root, text='Drag slider to adjust Interest Rate.')
rate_text.grid(row=4, columnspan=2, column=0)

# Instantiate and place Term(Years) slider
years_slider = Tkinter.Scale(root, from_=1, to=50, orient=HORIZONTAL, length=300, label='Years')
years_slider.grid(row=7, columnspan=2, column=0, sticky=Tkinter.W)
# Create and place directions for the user
years_text = Tkinter.Label(root, text='Drag slider to adjust term(years).')
years_text.grid(row=6, columnspan=2, column=0)

root.mainloop()