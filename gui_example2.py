from tkinter import *

"""
This sample application is written as a class.
The constructor (the __init__ method) is called with a parent widget
(the master), to which it adds a number of child widgets.
The constructor starts by creating a Frame widget.
A frame is a simple container, and is in this case only used to
hold the other two widgets.
"""
class App:
    def __init__(self, master):
        #The frame instance is stored in a local variable called frame. 
        #After creating the widget, 
        #we immediately call the pack method to make the frame visible.
        frame = Frame(master)

        #note this is a local variable, Tkinter
        #automatically maintains a widget tree
        #so a widget wont dissapear when the last
        #reference goes away
        frame.pack()


        #We then create two Button widgets, as children to the frame.

        # This time, we pass a number of options to the constructor, as keyword arguments. 
        # The first button is labelled “QUIT”,
        # and is made red (fg is short for foreground).
        # The second is labelled “Hello”. Both buttons also take a
        # command option. This option specifies a function, or 
        # (as in this case) a bound method, which will be called
        # when the button is clicked.
        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
        )

        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)


    def say_hi(self):
        ''' event handler for the hi_there button '''
        print("hi there, everyone!")

root = Tk()

app = App(root)

root.mainloop()

#optional
#desroy is only required if we run this example under
#certain development enviornments;
#it explicitly destroys the main windows when the
#event loop is terminated
root.destroy()