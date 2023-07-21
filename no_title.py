from tkinter import *
from tkinter import ttk

root = Tk()


def get_pos(event):
    xwin = root.winfo_x()
    ywin = root.winfo_y()
    startx = event.x_root
    starty = event.y_root

    ywin = ywin - starty
    xwin = xwin - startx

    def move_window(event):
        root.geometry("400x100" + '+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))

    startx = event.x_root
    starty = event.y_root

    title_bar.bind('<B1-Motion>', move_window)

# Define a function for resizing the window
def OnMotion(root):
    x1 = root.winfo_pointerx()
    y1 = root.winfo_pointery()
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    root.geometry("%sx%s" % ((x1-x0),(y1-y0)))
    return


root.overrideredirect(True) 
root.geometry('400x100+200+200') 

#title_bar = Frame(root, bg='white', relief='raised', bd=2)

#close_button = Button(title_bar, text='X', command=root.destroy)

window = Canvas(root, bg='black')

#title_bar.pack(expand=1, fill=X)
#close_button.pack(side=RIGHT)

window.pack(expand=1, fill=BOTH)

#title_bar.bind('<B1-Motion>', get_pos)
#title_bar.bind('<Button-1>', get_pos)


# Add the gripper for resizing the window
grip=ttk.Sizegrip()
grip.place(relx=1.0, rely=1.0, anchor="se")
grip.bind("<B1-Motion>", lambda event, r=root: OnMotion(r))

root.wm_attributes("-topmost", 1)

root.mainloop()



