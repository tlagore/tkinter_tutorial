import tkinter as tk

counter = 0 

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

    def counter_label(label):
        def count():
            global counter
            counter += 1
            label.config(text=str(counter))
            label.after(10, count)
        count()

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.title("Counting seconds")
    label = tk.Label(root, fg="blue")
    label.pack()
    MainApplication.counter_label(label)
    button = tk.Button(root, text='Stop', width=25, command=root.destroy)
    button.pack()
    root.mainloop()
