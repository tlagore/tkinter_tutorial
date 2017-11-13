import tkinter as tk
from tkinter import filedialog as tkfd

class Navbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initialize()
    def initialize(self):
        pass

class Toolbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initialize()
    def initialize(self):
        pass

class Statusbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.label = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.label.pack(fill=tk.X)
        
        self.initialize()
    
    def initialize(self):
        pass # initialize a window

    def set(self, txt, *args):
        self.label.config(text=txt)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        self.frame = tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initialize()
    
    def callback(self):
        name = tkfd.askopenfilename()
        print(name)
    
    def initialize(self):
        self.fButton = tk.Button(text='File Open', command=self.callback).pack(fill=tk.X)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        self.frame = tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.statusbar = Statusbar(self)
        self.toolbar = Toolbar(self)
        self.navbar = Navbar(self)
        self.main = Main(self)

        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)

        self.statusbar.set("wololo")

def windowszpos(root):
    w = 1200
    h = 700

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w,h,x,y))
    root.resizable(width=False, height=False)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    windowszpos(root)
    root.mainloop()
