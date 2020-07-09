# module import
from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np

model=Tk()
Label(model,text="Please inter your Name").grid(row=0,column=0,sticky=W)
Label(model,text="How much money you invest in market (Rs.)").grid(row=1,column=0,sticky=W)
Label(model,text="what is the rate of interest").grid(row=2,column=0,sticky=W)

#getting input in box
name_var=StringVar()
name_entry_box=Entry(model,width=18,textvariable=name_var).grid(row=0,column=1)
principle_var=IntVar()
Entry(model,width=18,textvariable=principle_var).grid(row=1,column=1)
interest_rate=IntVar()

model.mainloop()