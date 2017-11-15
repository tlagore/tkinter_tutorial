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
    
    def add_src_folder(self):
        folder_name = tkfd.askdirectory()
        if(folder_name):
            #for item
            # TODO need to check for duplicate entry 
            self.src_list.insert(END, folder_name)
        else:
            print("No folder selected!")

    def del_src_btn_clicked(self):
        lb = self.src_list
        #lambda lb=self.src_list: lb.delete(ANCHOR)
        selected = lb.curselection()
        if selected:
            lb.delete(selected)
        else:
            messagebox.showinfo("No sources selected", "You must select a source to remove one.")

        #lambda lb=self.src_list: lb.delete(ANCHOR)

    def choose_readw_loc(self):
        """ """
        file_name = tkfd.askopenfile()
        if(file_name):
            self.exe_field.configure(state="normal")
            #text box index location is noted by "row.column"
            self.exe_field.insert("0.0", str(file_name.name))
            self.exe_field.configure(state="disabled")

    def pick_dst_btn_clicked(self):
        """ """
        folder_name = tkfd.askdirectory()
        if(folder_name):
            #for item
            # TODO need to check for duplicate entry 
            self.dst_field.insert("0.0", str(folder_name))
        else:
            print("No folder selected!")
    
    def initialize(self):
        #self.grid(stick="nesw")

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(2, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_rowconfigure(2, weight=1)

        #### SOURCE FOLDER WIDGETS & BUTTONS #####
        self.src_lbl = tk.Label(self.parent, text="Source Folders")
        #sets background of this element to be the same background as the parent color
        #note that self.parent["bg"] returns parents background color. 
        #More generally, widget["bg"]. Alternate way of writing this is self.src_lbl["bg"] = self.parent["bg"]
        self.src_lbl.configure(background=self.parent["bg"])

        #padx=(left,right) <- pads the cell with tuple for left/right pad
        #pady=(top, bottom) <- pads the cell with tuple for top/bottom pad
        self.src_lbl.grid(row=0, column=0, columnspan=3, padx=(10,10), pady=(10,0), sticky=W)

        ##listbox, this maintains a list of clickable items - these will be the source folders
        ##height is set to 5x the height of a label, should be able to view 5 source folders in a window
        self.src_list = tk.Listbox(self.parent, height=5)#, height=int(self.src_lbl.winfo_height()*5))
        self.src_list.grid(row=1, column = 0, rowspan=2, padx=(10,10), pady=(0,10), sticky="we")
        self.src_list.insert(END, "C:/Sample/Directory")
        ##end listbox
        self.add_src_btn = tk.Button(
            self.parent, text="Add Folder", width=15, command=self.add_src_folder
        )

        # find default button height################
        self.btn_height = self.add_src_btn.winfo_height()
        ############################################

        self.del_src_btn = tk.Button(
            self.parent, text="Remove Folder", width=15, 
            command=self.del_src_btn_clicked
        )
        self.add_src_btn.grid(row=1, column=2, padx=(10,10), sticky=N)
        self.del_src_btn.grid(row=2, column=2, padx=(10,10), pady=(0,10), sticky=N)
        #Style().configure("TButton", padding=(10,10,10,10))

        ### END SOURCE FOLDERS WIDGETS & BUTTONS ###
        

        ### start pick_exe section ###
        self.exe_lbl = tk.Label(self.parent, text="ReAdW.exe Location")
        self.exe_lbl.configure(background=self.parent["bg"])
        self.exe_lbl.grid(row=3, column = 0, padx=(10,10), pady=(10,0), sticky=W)

        self.exe_field = tk.Text(self.parent, height=self.btn_height, state="disabled")
        self.exe_field.grid(row=4, column=0, columnspan=1, padx=(10,10), sticky="we")

        self.pick_exe_btn = tk.Button(
            self.parent, text="Choose Location", width=15, command=self.choose_readw_loc
        )
        self.pick_exe_btn.grid(row=4, column=2)

        ### END pick_exe section ###

        ### start pick destination section ###
        ##Note columnspan=2, this tells the grid manaeger to span this widget over 2 
        ##It will appear centered in row 0 and row 1.
        self.dst_lbl = tk.Label(self.parent, text="Destination") 
        self.dst_lbl.configure(background=self.parent["bg"])
        self.dst_lbl.grid(row=6, column=0, columnspan=2, padx=(10,10), pady=0, sticky="w")

        self.dst_field = tk.Text(self.parent, height=self.btn_height, state="disabled")
        self.dst_field.grid(row=7, column = 0, columnspan=1, padx=(10,10), pady=(0,10), sticky="we")

        self.pick_dst_btn = tk.Button(
            self.parent, text="Choose Destination", width=15, command=self.pick_dst_btn_clicked
        )
        self.pick_dst_btn.grid(row=7, column=2)

if __name__ == "__main__":
    root = tk.Tk()
    #window_config(root)
    MainApplication(root).grid(stick="nesw")
    """
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(1, weight=1)
    """

    root.winfo_toplevel().title("MIA")
    #uncomment if we make window resizable
    #set min width/height to current width/height
    root.update()
    #unecessary as window is not resizable, but if we remove resizable, window cant be smaller than default
    #root.minsize(root.winfo_width(), root.winfo_height())

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    w = root.winfo_width()
    h = root.winfo_height()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w,h,x,y))
    root.resizable(False, False)

    root.mainloop()
