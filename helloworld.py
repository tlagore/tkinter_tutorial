from tkinter import *

root = Tk()

logo = PhotoImage(file="13.png")
w1 = Label(root, image = logo).pack(side="right")
explanation = """At Present, only PNG and GIF 
formats are supported, but an interface 
exists to allow additional image file formats 
to be added easily."""
w2 = Label(root,
           justify=LEFT,
           padx=10,
           text=explanation).pack(side="left")
root.mainloop()
