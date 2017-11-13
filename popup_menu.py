from tkinter import *

root = Tk()

def hello():
    print("hello!")

# create a popup menu
menu = Menu(root, tearoff=0)
menu.add_command(label="Undo", command=hello)
menu.add_command(label="Redo", command=hello)

# create a canvas
frame = Frame(root, width=512, height=512)
frame.pack()

def popup(event):
    menu.post(event.x_root, event.y_root)

# attach popup to canvas
# rightclick makes menu come up
frame.bind("<Button-3>", popup)

root.mainloop()

""" REFERENCE:::::::
Reference #

Menu(master=None, **options) (class) [#]

    A menu pane.
__init__(master=None, **options) [#]

    Creates a menu widget.

    master
        Parent widget.
    **options
        Widget options. See the description of the config method for a list of available options.


activate(index) [#]

    The activate method.

    index


add(type, **options) [#]

    Add (append) an entry of the given type to the menu.

    type
        What kind of entry to add. Can be one of “command”, “cascade” (submenu), “checkbutton”, “radiobutton”, or “separator”. 
    **options
        Menu options.
    activebackground=
    activeforeground=
    accelerator=
    background=
    bitmap=
    columnbreak=
    command=
    font=
    foreground=
    hidemargin=
    image=
    indicatoron=
    label=
    menu=
    offvalue=
    onvalue=
    selectcolor=
    selectimage=
    state=
    underline=
    value=
    variable=


add_cascade(**options) [#]

    Adds a submenu. See add for a list of options.

    **options


add_checkbutton(**options) [#]

    Adds a checkbutton. See add for a list of options.

    **options


add_command(**options) [#]

    Adds a command. See add for a list of options.

    **options


add_radiobutton(**options) [#]

    Adds a radiobutton. See add for a list of options.

    **options


add_separator(**options) [#]

    Adds a separator. See add for a list of options.

    **options


config(**options) [#]

    Modifies one or more widget options. If no options are given, the method returns a dictionary containing all current option values.

    **options
        Widget options.
    activebackground=
        Default value is ‘SystemHighlight’. (the database name is activeBackground, the class is Foreground)
    activeborderwidth=
        Default value is 0. (activeBorderWidth/BorderWidth)
    activeforeground=
        Default value is ‘SystemHighlightText’. (activeForeground/Background)
    background=
        Default value is ‘SystemMenu’. (background/Background)
    bg=
        Same as background.
    borderwidth=
        Default value is 0. (borderWidth/BorderWidth)
    bd=
        Same as borderwidth.
    cursor=
        Default value is ‘arrow’. (cursor/Cursor)
    disabledforeground=
        Default value is ‘SystemDisabledText’. (disabledForeground/DisabledForeground)
    font=
        Default value is ‘MS Sans Serif 8’. (font/Font)
    foreground=
        Default value is ‘SystemMenuText’. (foreground/Foreground)
    fg=
        Same as foreground.
    postcommand=
        No default value. (postCommand/Command)
    relief=
        Default value is ‘flat’. (relief/Relief)
    selectcolor=
        Default value is ‘SystemMenuText’. (selectColor/Background)
    takefocus=
        Default value is 0. (takeFocus/TakeFocus)
    tearoff=
        Default value is 1. (tearOff/TearOff)
    tearoffcommand=
        No default value. (tearOffCommand/TearOffCommand)
    title=
        No default value. (title/Title)
    type=
        Default value is ‘normal’. (type/Type)


delete(index1, index2=None) [#]

    Deletes one or more menu entries.

    index1
        The first entry to delete.
    index2
        The last entry to delete. If omitted, only one entry is deleted.


entrycget(index, option) [#]

    The entrycget method.

    index
    option


entryconfig(index, **options) [#]

    Reconfigures the given menu entry. Only the given options are changed; the rest are left as is. See add for a list of available options.

    index
    **options


entryconfigure(index, **options) [#]

    Same as entryconfig (dead link). 
index(index) [#]

    Converts an index (of any kind) to an integer index.

    index
    Returns:
        An integer index.


insert(index, itemType, **options) [#]

    Inserts an entry of the given type in the menu. This is similar to add, but inserts an entry

    index
    itemType
    **options


insert_cascade(index, **options) [#]

    Inserts a submenu.

    index
    **options


insert_checkbutton(index, **options) [#]

    Inserts a checkbutton.

    index
    **options


insert_command(index, **options) [#]

    Inserts a command.

    index
    **options


insert_radiobutton(index, **options) [#]

    Inserts a radiobutton.

    index
    **options


insert_separator(index, **options) [#]

    Inserts a separator. def insert_separator(index, **options)

    index
    **options


invoke(index) [#]

    The invoke method.

    index


post(x, y) [#]

    Displays the menu at the given position. The position should be given in pixels, relative to the root window.

    x
        Menu position.
    y
        Menu position.


type(index) [#]

    Gets the type of the given menu entry.

    index
        Index specifier.
    Returns:
        Item type.


unpost() [#]

    Removes a posted menu.
yposition(index) [#]

    Returns the vertical offset for the given entry. This can be used to position a popup menu so that a given entry is under the mouse when the menu appears.

    index
        Index specifier.
    Returns:
        The vertical offset, in screen coordinates. 

"""