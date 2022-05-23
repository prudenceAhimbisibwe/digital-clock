import sys
from tkinter import *
import time

def timing():
    current_time= time.strftime("%H : %M : %S")
    clock.config(text=current_time)
    #clock will change after every 100 microseconds
    clock.after(100,timing)

root=Tk()
root.geometry("600x300")
clock=Label(root,font=("times",60,"bold"),bg="green")
clock.grid(row=2,column=2,pady=25,padx=100)
timing()

digital=Label(root,text="Ash python's Digital Clock",font="times 24 bold")
digital.grid(row=0,column=2)

nota=Label(root,text="hours     minutes     seconds",font="times 15 bold")
nota.grid(row=3,column=2)

root.mainloop()