from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

redbutton = Button(frame, text="Red", fg="red", relief=RIDGE)
redbutton.pack(side=LEFT)

# Syntax
#
# Here is the simple syntax to create this widget −
#
# w = LabelFrame( master, option, ... )
#
# Parameters
#
#     master: This represents the parent window.
#
#     options: Here is the list of most commonly used options for this widget.
#     These options can be used as key-value pairs separated by commas.
#
# Option	            Description
# bg	                The normal background color displayed behind the label
#                       and indicator.
# bd                	The size of the border around the indicator. Default
#                       is 2 pixels.
# cursor	            If you set this option to a cursor name (arrow, dot
#                       etc.), the mouse cursor will change to that pattern
#                       when it is over the checkbutton.
# font	                The vertical dimension of the new frame.
# height	            The vertical dimension of the new frame.
# labelAnchor 	        Specifies where to place the label.
# highlightbackground	Color of the focus highlight when the frame does not
#                       have focus.
# highlightcolor	    Color shown in the focus highlight when the frame has
#                       the focus.
# highlightthickness	Thickness of the focus highlight.
# relief	            With the default value, relief=FLAT, the checkbutton
#                       does not stand out from its background. You may set
#                       this option to any of the other styles
# text	                Specifies a string to be displayed inside the widget.
# width	                Specifies the desired width for the window.

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack(side=LEFT)

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack(side=LEFT)

blackbutton = Button(bottomframe, text="Black", fg="black")

blackbutton.pack(expand=True,   # When set to true, widget expands to fill any
                                # space not otherwise used in widget's parent.

                 fill=X,        # Determines whether widget fills any extra
                                # space allocated to it by the packer, or keeps
                                # its own minimal dimensions: NONE (default),
                                # X (fill only horizontally), Y (fill only
                                # vertically), or BOTH (fill both horizontally
                                # and vertically).

                 side=BOTTOM    # Determines which side of the parent widget
                                # packs against: TOP (default), BOTTOM, LEFT,
                                # or RIGHT.
                 )

root.mainloop()
