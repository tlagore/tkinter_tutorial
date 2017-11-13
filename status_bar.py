from tkinter import *

class StatusBar(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, txt, *args):
        self.label.config(text=txt)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()


root = Tk()
status = StatusBar(root)
status.set("wololo")
status.pack(side=BOTTOM, fill=X)
root.mainloop()