from tkinter import *
from tkinter import messagebox

def callback():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()

root = Tk()
#window not resizable
root.resizable(width=False, height=False)

#set window size
root.geometry('{}x{}'.format(500,500))
root.protocol("WM_DELETE_WINDOW", callback)


root.mainloop()

# more tutorial jazz
# https://www.tutorialspoint.com/python3/python_gui_programming.htm

""" 
    The pack() Method − 
    This geometry manager organizes widgets in blocks before placing them in the parent widget.

    The grid() Method − 
    This geometry manager organizes widgets in a table-like structure in the parent widget.

    The place() Method − 
    This geometry manager organizes widgets by placing them in a specific position in the parent widget.

"""