from tkinter import Tk 
from tkinter import Label
import time
import sys

master = Tk ()
master.title("Digital Clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)

clock = Label(master, font=("Times New Roman",90),bg="gray",fg="skyblue")
clock.pack()


get_time()
master.mainloop()
