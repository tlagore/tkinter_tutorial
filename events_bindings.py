#wdigget configuration
#usually use optionos rather than method calls
#widgetclass(master, option=value,...)

from tkinter import *

root = Tk()

def key(event):
    print("Pressed key: {}".format(repr(event.char)))

def callback(event):
    frame.focus_set()
    print("Clicked at {}, {}".format(event.x, event.y))


#Events are all given as strings using a special event syntax:
#<modifier-type-detail>
frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.bind("<Key>", key)
frame.pack()

root.mainloop()

#notable formats
# <Button-1> 
# (button 1 is left most, 2 is middle, 3 is right most)
# <B1-Motion> - mouse is moved with button 1 held down
# (think dragging)
# <Enter> - mouse entered widget
# <ButtonRelease-1> button 1 was released,
# in the above event, mouse x and y is in event
#
# <Leave> mouse left the widget
#
# <FocusIn>, keyboard focus moved to this widget
#
# <FocusOut> Keyboard focus moved out
#
# <Return> User pressed enter key.
#  You can bind this to basically any key on the keyboard
#
# <Shift-Up>, use pressed up while shift was held

'''
The Event Object

The event object is a standard Python object instance, with a number of attributes describing the event.
Event Attributes

widget

    The widget which generated this event. This is a valid Tkinter widget instance, not a name. This attribute is set for all events.
x, y

    The current mouse position, in pixels.
x_root, y_root

    The current mouse position relative to the upper left corner of the screen, in pixels.
char

    The character code (keyboard events only), as a string.
keysym

    The key symbol (keyboard events only).
keycode

    The key code (keyboard events only).
num

    The button number (mouse button events only).
width, height

    The new size of the widget, in pixels (Configure events only).
type

    The event type.

For portability reasons, you should stick to char, height, width, x, y, x_root, y_root, and widget. Unless you know exactly what you’re doing, of course…
Instance and Class Bindings
'''