from tkinter import *
import tkinter.messagebox

top = tkinter.Tk()

def helloCallBack():
    tkinter.messagebox.showinfo("Hello Python", "Hello World")

B = tkinter.Button(top, text="Hello", command=helloCallBack)

B.pack()
B.place(anchor=W,           # The exact spot of widget other options refer to:
                            # may be N, E, S, W, NE, NW, SE, or SW, compass
                            # directions indicating the corners and sides of
                            # widget; default is NW (the upper left corner of
                            # widget)
        bordermode=OUTSIDE, # INSIDE (the default) to indicate that other
                            # options refer to the parent's inside
                            # (ignoring the parent's border);OUTSIDE otherwise.
        height=50,          # Height and width in pixels.
        width=100,

        relheight=0.2,      # Height and width as a float between 0.0 and 1.0,
        relwidth=0.4,       # as a fraction of the height and width of the
                            # parent widget.

        relx=0.1,           # Horizontal and vertical offset as a float between
        rely=0.3,           # 0.0 and 1.0, as a fraction of the height and
                            # width of the parent widget.

        x=1,                # Horizontal and vertical offset in pixels.
        y=1
        )

top.mainloop()