""" """
from tkinter import *

root = Tk()

mLabel = Label(root, text="Hello World!")
#pack tells the label to size itself to fit
# the given text and make itself visible 
mLabel.pack()

root.mainloop()