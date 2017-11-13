from tkinter import *
from tkinter import messagebox


messagebox.showinfo(
    "Open file",
    "Yo dude this is some mad info."
)

messagebox.showwarning(
    "Open file",
    "Yo dude this is a mad warning."
)

messagebox.showerror(
    "Open file",
    "Yo dude this is a mad error."
)

if messagebox.askyesno("CLick Yes", "Fucking click yes you asshole"):
    messagebox.showinfo("THANKS", "Awwww yisssss.")
else:
    messagebox.showerror("Fuck you you shitter", "You heard me, you're a shitter")