import binascii
from Crypto.Cipher import AES
import getpass
import PySimpleGUI as sg
from tkinter import *
from tkinter import filedialog
import json
from getkey import getkey, key
sg.theme('SystemDefault1')



# Create the main window
window = Tk()

# Create the menu bar
menu_bar = Menu(window)

# Create the menu Menu1
menu_1 = Menu(menu_bar, tearoff=0)

# Create a photo image
item_1_icon = PhotoImage(file="C:\\Users\\frolov.an\\Desktop\\icon.png")

# Add items for Menu1
menu_1.add_command(label="Item1", image=item_1_icon, compound="left")
menu_1.add_cascade(label="Item2")

# Add the menu to the menu bar
menu_bar.add_cascade(label="Menu1", menu=menu_1)

# Attach the menu bar to the main window
window.config(menu=menu_bar)

# Start the Tkinter event loop
window.mainloop()