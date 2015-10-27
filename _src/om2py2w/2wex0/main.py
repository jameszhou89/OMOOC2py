#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)




    def say_hi(self):
        print "hi there, everyone!"

root = Tk()

app = App(root)

e = Entry(root,width=50)
e.pack()

e.focus_set()

def callback():
    print e.get()

b = Button(root, text="get", width=10, command=callback)
b.pack()

root.mainloop()
root.destroy() # optional; see description below