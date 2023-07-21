from tkinter import Tk, Label, Menu, ttk
from tkinter.font import Font
from random import SystemRandom

FONTSIZE_INCR = 15
menu_isvisible = True
color_mode = False
rng_istimed = False
rng_limit = (1, 100)

def main():
    root = Tk()
    root.title('RNGclick')

    fontStyle = Font(family='Consolas', size=80)
    label = Label(root, text="0", font=fontStyle, bg='black')
    label.pack(expand='True', fill="both")

    emptyMenu = Menu(root)
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Quit", command=lambda r=root: close(r))
    filemenu.add_separator()
    filemenu.add_command(label="Switch Color Order", command=color_switch)
    filemenu.add_separator()
    filemenu.add_radiobutton(label="RNG from 0-99", command=lambda: rng_limit_switch((0,99)))
    filemenu.add_radiobutton(label="RNG from 1-100", command=lambda: rng_limit_switch((1,100)))
    filemenu.add_separator()
    filemenu.add_command(label="Increase Font Size", command=lambda: fontStyle.config(size = fontStyle['size'] + FONTSIZE_INCR))
    filemenu.add_command(label="Decrease Font Size", command=lambda: fontStyle.config(size = fontStyle['size'] - FONTSIZE_INCR))
    filemenu.add_separator()
    filemenu.add_command(label="Timed Mode Toggle", command=timed_switch)
    menubar.add_cascade(label="Options", menu=filemenu)
    root.config(menu=menubar)

    root.configure(background='black')
    root.bind('<Button-1>', lambda event, r=root, l=label: gen_rand(r, l))
    #root.bind('<Double-Button-1>', lambda event,  r=root, e=emptyMenu, m=menubar: remove_header(r, e, m))
    root.bind('<Button-3>', lambda event, l=label: clear_rand(l))
    root.bind('<Double-Button-3>', lambda event, r=root, e=emptyMenu, m=menubar: menu_switch(r, e, m))

#remove title bar 
    root.overrideredirect(True) #
    root.update()
    root.attributes('-topmost', True)

    #root.geometry("260x200+200+200")
    center_window(root,200,200)

# Add the gripper for resizing the window
    grip=ttk.Sizegrip()  #
    grip.place(relx=1.0, rely=1.0, anchor="se")#
    grip.bind("<B1-Motion>", lambda event, r=root: OnMotion(r))#
    
    #root.wm_attributes("-topmost", 1)
    gen_rand(root, label)
    root.mainloop()



# Define a function to close the window
def close(root):
   #win.destroy()
   root.quit()

def center_window(root, width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def gen_rand(root, label):
    global rng_istimed, color_mode, rng_limit
    COLORS = ('#FF3333','#FFAC33','#FFFF33','#33FF39','#33FF39','#FFFF33','#FFAC33','#FF3333')

    label['text'] = SystemRandom().randint(rng_limit[0], rng_limit[1])
    label.config(fg=COLORS[(label['text'] + 100*int(color_mode) - rng_limit[0]) // 25])
    if rng_istimed:
        root.after(3000, lambda: gen_rand(root, label))

def clear_rand(label):
	label['text'] = ""

def color_switch():
    global color_mode
    color_mode = not(color_mode)

def timed_switch():
    global rng_istimed
    rng_istimed = not(rng_istimed)

def rng_limit_switch(new_limit):
    global rng_limit
    rng_limit = new_limit


def remove_header(root, emptyMenu, menubar): #
    root.config(menu=menubar)
    root.geometry("260x200+200+200")
    root.wm_attributes("-topmost", 1)
    root.overrideredirect(1)
    root.overrideredirect(0)



def OnMotion(root): #
    x1 = root.winfo_pointerx()
    y1 = root.winfo_pointery()
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    root.geometry("%sx%s" % ((x1-x0),(y1-y0)))
    return

def menu_switch(root, emptyMenu, menubar):
    global menu_isvisible
    if menu_isvisible:
        root.config(menu=emptyMenu)
        menu_isvisible = not menu_isvisible
        winx = root.winfo_rootx() - 1
        winy = root.winfo_rooty() + 19
        winw = root.winfo_width()
        winh = root.winfo_height() - 38
        root.geometry(f'{winw}x{winh}')
        root.geometry(f'+{winx}+{winy}')
        root.overrideredirect(1)
    else:
        root.config(menu=menubar)
        menu_isvisible = not menu_isvisible
        winx = root.winfo_rootx() - 7
        winy = root.winfo_rooty() - 50
        winw = root.winfo_width()
        winh = root.winfo_height() - 2
        root.geometry(f'{winw}x{winh}')
        root.geometry(f'+{winx}+{winy}')
        root.overrideredirect(0)

if __name__ == '__main__':
    main()
