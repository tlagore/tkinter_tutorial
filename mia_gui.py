import tkinter as tk
from tkinter import *
from tkinter import messagebox
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
    
    def add_src_folder(self):
        folder_name = tkfd.askdirectory()
        if(folder_name):
            #for item
            # TODO need to check for duplicate entry 
            self.src_list.insert(END, folder_name)
        else:
            print("No folder selected!")

    
    def initialize(self):
        #self.grid(row=1, column=1, sticky="nsew")

        self.grid_rowconfigure(0, pad=15, weight=1)
        self.grid_columnconfigure(0, pad=15, weight=1)

        self.src_lbl = tk.Label(self.parent, width=25, text="Source Folders")
        #sets background of this element to be the same background as the parent color
        #note that self.parent["bg"] returns parents background color. 
        #Moe generally, widget["bg"]. Alternate way of writing this is self.src_lbl["bg"] = self.parent["bg"]
        self.src_lbl.configure(background=self.parent["bg"])

        #padx=(left,right) <- pads the cell with tuple for left/right pad
        #pady=(top, bottom) <- pads the cell with tuple for top/bottom pad (not sure if its top/bottom or bottom/top)
        self.src_lbl.grid(row=0, column=0, padx=(10,10), pady=(10,10))
        
        self.exe_lbl = tk.Label(self.parent, width=25, text="ReAdW.exe Location")
        self.exe_lbl.configure(background=self.parent["bg"])
        self.exe_lbl.grid(row=2, column = 0, padx=(10,10), pady=(10,10))

        ##Note columnspan=2, this tells the grid manaeger to span this widget over 2 
        ##It will appear centered in row 0 and row 1.
        self.dst_lbl = tk.Label(self.parent, width=25, text="Destination") 
        self.dst_lbl.configure(background=self.parent["bg"])
        self.dst_lbl.grid(row=3, column=0, columnspan=2, padx=(10,10), pady=(10,10))
        
        ##listbox, this maintains a list of clickable items - these will be the source folders
        ##height is set to 5x the height of a label, should be able to view 5 source folders in a window
        self.src_list = tk.Listbox(self.parent, width=50, height=int(self.src_lbl.winfo_height()*5))
        self.src_list.grid(row=0, column = 1, rowspan=2, padx=(10,10), pady=(10,10))
        self.src_list.insert(END, "C:/Sample/Directory")
        ##end listbox
        self.add_src_btn = tk.Button(
            self.parent, text="Add Folder", width=15, command=self.add_src_folder
        )
        self.del_src_btn = tk.Button(
            self.parent, text="Remove Folder", width=15, 
            command=lambda lb=self.src_list: lb.delete(ANCHOR)
        )
        self.add_src_btn.grid(row=0, column=2, padx=(10,10), pady=(10,10))
        self.del_src_btn.grid(row=1, column=2, padx=(10,10), pady=(10,10))
    
        
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        self.frame = tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid(sticky="nsew")#, row=0, column=1)
        self.grid_rowconfigure(1, pad=10, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.main = Main(self)
        #self.main.grid(row=0, column=0, sticky="nsew")
        #self.statusbar = Statusbar(self, bg="orange")
        #self.toolbar = Toolbar(self, bg="blue")
        #self.navbar = Navbar(self)
        self.initEventHandlers()
    
    def initEventHandlers(self):
        self.parent.protocol("WM_DELETE_WINDOW", self.exit)

    def exit(self):
        if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            root.destroy()

def window_config(root):
    #center window and lock dimensions
    #w = 800
    #h = 500

    #ws = root.winfo_screenwidth()
    #hs = root.winfo_screenheight()

    #x = (ws/2) - (w/2)
    #y = (hs/2) - (h/2)

    #root.geometry('%dx%d+%d+%d' % (w,h,x,y))
    #root.resizable(width=False, height=False)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.winfo_toplevel().title("MIA")

if __name__ == "__main__":
    root = tk.Tk()
    window_config(root)
    MainApplication(root, bg='lightgray')

    #set min width/height to current width/height
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())

    root.mainloop()
