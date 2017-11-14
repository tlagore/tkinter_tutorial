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
        self.grid(row=0, sticky="ew")

class Statusbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initialize()
    
    def initialize(self):
        self.grid(row=3, sticky="ew")
        self.label = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)

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
        name = tkfd.askdirectory()
        print(name)
    
    def initialize(self):
        self.grid(row=2, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.src_lbl = tk.Label(self.parent, text="Source Folder", bg="red")
        self.src_lbl.grid(sticky="e")
        self.exe_lbl = tk.Label(self.parent, text="Program", bg="yellow")
        self.exe_lbl.grid(sticky="e")
        self.dst_lbl = tk.Label(self.parent, text="Destination", bg="green") 
        self.dst_lbl.grid(sticky="e")
        
        
        #self.fButton = tk.Button(text='File Open', command=self.callback).pack()

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        self.frame = tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.main = Main(self, bg="purple")
        self.statusbar = Statusbar(self, bg="orange")
        self.toolbar = Toolbar(self, bg="blue")
        self.navbar = Navbar(self)
        
        

def window_config(root):
    #center window and lock dimensions
    w = 800
    h = 500

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w,h,x,y))
    root.resizable(width=False, height=False)

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.winfo_toplevel().title("MIA")

if __name__ == "__main__":
    root = tk.Tk()
    window_config(root)
    MainApplication(root, bg='cyan')
    root.mainloop()
