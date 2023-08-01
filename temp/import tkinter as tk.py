#Import the Tkinter Library
from tkinter import *

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry of window
win.geometry("700x350")

#Define a callback function for exit
def quit_program(e):
   win.destroy()

#Add a Label widget
# label = Label(win, text= "Press Ctrl + x to Exit", font= ('Helvetica 15 bold'))
# label.pack(pady= 40)

#Bind the Keyboard shortcut Key
win.bind('<Control-x>', quit_program)
win.mainloop()