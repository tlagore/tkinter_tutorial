import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as tkfd
from tkinter.ttk import Style
from tkinter import ttk



class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        self.frame = tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initialize()
    
    def initialize(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(1, weight=2)

        self.lst_bx = tk.Listbox(self.parent, height = 3)
        self.lst_bx.grid(row=0, column=0, columnspan=1, padx=(10,10), sticky="ew")

        self.exe_field = tk.Text(self.parent, width=25, height = 3)
        self.exe_field.grid(row=1, column=0, columnspan=1, padx=(10,10), sticky="ew")

        self.pick_exe_btn = tk.Button(
            self.parent, text="Choose Location", width=15
        )
        self.pick_exe_btn.grid(row=0, column=1)

        

if __name__ == "__main__":
    root = tk.Tk()
    #window_config(root)
    MainApplication(root).grid(stick="nesw")
    root.resizable(False, False)

    root.mainloop()
