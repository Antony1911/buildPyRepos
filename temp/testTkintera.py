import binascii
from Crypto.Cipher import AES
import getpass
import PySimpleGUI as sg
from tkinter import *
from tkinter import filedialog
import json
from getkey import getkey, key
sg.theme('SystemDefault1')

root = Tk()
fram = Frame(root)

root.title('test_Wwindow')
root.geometry("400x400+700+40")

# Label(fram,text='Text to find: ',).pack(side=LEFT)
# edit = Entry(fram, width=40)
# edit.pack(side=LEFT, fill=BOTH, expand=1)

# buttClear = Button(fram, text='Clear', bg='yellow') 
# buttClear.pack(side=RIGHT)

# buttFind = Button(fram, text='Find', bg='green') 
# buttFind.pack(side=RIGHT)

fram.pack(side=TOP)
v = Scrollbar(root, orient = 'vertical')
v.pack(side=RIGHT, fill = 'y')


text = Text(root, height=40, width=70, font=('Consolas',14), yscrollcommand=v.set)
v.config(command=text.yview)
text.pack(expand=True)

root.mainloop()
root.destroy()