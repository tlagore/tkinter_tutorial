import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as tkfd
from tkinter.ttk import Style
from tkinter import ttk



class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parnet = parent
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
        self.main_lbl = tk.Label(self, text="Mama Mia!")
        self.main_lbl.grid(row=0, column=0, columnspan=3)
        self.main_lbl.config(font=("Garamond", 36))

        #### SOURCE FOLDER WIDGETS & BUTTONS #####
        self.src_lbl = tk.Label(self, text="Source Folders")
        #sets background of this element to be the same background as the parent color
        #note that self["bg"] returns parents background color. 
        #More generally, widget["bg"]. Alternate way of writing this is self.src_lbl["bg"] = self["bg"]
        self.src_lbl.configure(background=self["bg"])

        #padx=(left,right) <- pads the cell with tuple for left/right pad
        #pady=(top, bottom) <- pads the cell with tuple for top/bottom pad
        self.src_lbl.grid(row=1, column=0, columnspan=3, padx=20, pady=(0,0), sticky=W)

        #self.src_scrll = Scrollbar(self, orient=VERTICAL)

        ##listbox, this maintains a list of clickable items - these will be the source folders
        ##height is set to 5x the height of a label, should be able to view 5 source folders in a window
        self.src_list = tk.Listbox(self, height=5)#, yscrollcommand=self.src_scrll.set)
        self.src_list.grid(row=2, column = 0, rowspan=2, padx=20, pady=0, sticky="we")
        
        #self.src_scrll.config(command=self.src_list.yview)
        #self.src_scrll.grid(row=1, column=0)
        
        self.src_list.insert(END, "C:/Sample/Directory")
        ##end listbox
        self.add_src_btn = tk.Button(
            self, text="Add Folder", width=15, command=self.add_src_folder
        )

        # find default button height################
        self.btn_height = self.add_src_btn.winfo_height()
        ############################################

        self.del_src_btn = tk.Button(
            self, text="Remove Folder", width=15, 
            command=self.del_src_btn_clicked
        )
        self.add_src_btn.grid(row=2, column=2, padx=20, sticky=N)
        self.del_src_btn.grid(row=3, column=2, padx=20, pady=(20,0), sticky=S)
        #Style().configure("TButton", padding=(10,10,10,10))

        ### END SOURCE FOLDERS WIDGETS & BUTTONS ###
        

        ### start pick_exe section ###
        self.exe_lbl = tk.Label(self, text="ReAdW.exe Location")
        self.exe_lbl.configure(background=self["bg"])
        self.exe_lbl.grid(row=4, column = 0, padx=20, pady=(0,0), sticky=W)

        self.exe_field = tk.Text(self, height=self.btn_height, width=50, state="disabled")
        self.exe_field.grid(row=5, column=0, columnspan=1, padx=20, sticky="w")

        self.pick_exe_btn = tk.Button(
            self, text="Choose Location", width=15, command=self.choose_readw_loc
        )
        self.pick_exe_btn.grid(row=5, column=2)

        ### END pick_exe section ###

        ### start pick destination section ###
        ##Note columnspan=2, this tells the grid manaeger to span this widget over 2 
        ##It will appear centered in row 0 and row 1.
        self.dst_lbl = tk.Label(self, text="Destination") 
        self.dst_lbl.configure(background=self["bg"])
        self.dst_lbl.grid(row=7, column=0, columnspan=2, padx=20, pady=0, sticky="w")

        self.dst_field = tk.Text(self, height=self.btn_height, width=50, state="disabled")
        self.dst_field.grid(row=8, column = 0, columnspan=1, padx=20, pady=(0,20), sticky="w")

        self.pick_dst_btn = tk.Button(
            self, text="Choose Destination", width=15, command=self.pick_dst_btn_clicked
        )
        self.pick_dst_btn.grid(row=8, column=2, pady=(0,20))
        ###end pick desitnation section ###

        ### start interval section ###
        self.interval_lbl = tk.Label(self, text="Transfer Interval (Minutes)")
        self.interval_lbl.configure(background=self["bg"])
        self.interval_lbl.grid(row=9, column=0, columnspan=2, padx=20, pady=0, sticky="w")

        self.interval_slider = tk.Scale(self, from_=5, to=45, orient=HORIZONTAL)
        self.interval_slider.grid(row=10, column=0, padx=20, pady=(0,20), sticky="ew")

        ### end interval section ###

        self.parallel_frame = tk.Frame(self)
        self.parallel_frame.grid(row=10, column=2)

        self.parallel_lbl = tk.Label(self.parallel_frame, text="Parallelize")
        self.parallel_lbl.grid(row=0, column=0, padx=(0,10))

        self.parallel_chkbx = tk.Checkbutton(self.parallel_frame)
        self.parallel_chkbx.grid(row=0, column=1, padx=(10,10))

        ### start control button settings ###        
        self.ctrl_frame = tk.Frame(self, highlightbackground='darkgray', highlightcolor='darkgray', highlightthickness=1)
        self.ctrl_frame.grid(row=11, column=0, columnspan=3, pady=(0,20))

        ### default to disabled, enable when stop is pressed ###
        self.start_btn = tk.Button(
            self.ctrl_frame, text="Start Mia", width=15, command=None, state="disabled"
        )

        self.stop_btn = tk.Button(
            self.ctrl_frame, text="Stop Mia", width=15, command=None
        )
        self.restart_btn = tk.Button(
            self.ctrl_frame, text="Restart Mia", width=15, command=None
        )

        self.start_btn.grid(row=0, column=0, columnspan=1, padx=(50,40), pady=(20,20))
        self.stop_btn.grid(row=0, column=1, columnspan=1, padx=(20,20), pady=(20,20))
        self.restart_btn.grid(row=0, column=2, columnspan=1, padx=(40,50), pady=(20,20))
        ### end control button settings ###

        self.status_frame = tk.Frame(self, highlightbackground='darkgray', highlightcolor='darkgray', highlightthickness=1)
        self.status_frame.grid(row=12, column=0, columnspan=3, sticky="ew")

        self.status_frame.columnconfigure(0,weight=1)

        self.status_lbl = tk.Label(self.status_frame, text="Status", width=15)
        self.status_lbl.grid(row=0,column=0)

        #status list box holds 5 items (change with width=x)
        self.status_list_box = tk.Listbox(self.status_frame, background=self["bg"], height=5)
        self.status_list_box.grid(row=1,column=0, columnspan=3, sticky="nsew")

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

    #ws = root.winfo_screenwidth()
    #hs = root.winfo_screenheight()

    #w = root.winfo_width()
    #h = root.winfo_height()

    #x = (ws/2) - (w/2)
    #y = (hs/2) - (h/2)

    #root.geometry('%dx%d+%d+%d' % (w,h,x,y))
    root.resizable(False, False)

    root.mainloop()
