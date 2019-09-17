import tkinter as t
from tkinter import *

from tkinter import messagebox  
def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    messagebox.showinfo("master", "whatever_you_do")

master = t.Tk()
master.geometry("500x500")

t.Label(master, text="First Name").grid(row=0)
t.Label(master, text="Last Name").grid(row=1)
t.Label(master, text="First Name").grid(row=3)

e1 = t.Entry(master)
e2 = t.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

t.Button(master, text='Quit', command=master.quit,bg="red").grid(
    row=4, column=0, sticky=t.W, pady=4)
t.Button(master, text='Show', command=show_entry_fields).grid(
    row=4, column=1, sticky=t.W, pady=4)

t.mainloop()
