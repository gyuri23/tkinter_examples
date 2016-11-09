import tkinter

root = tkinter.Tk()
for r in range(3):
    for c in range(5):
        tkinter.Label(root, text='R%s/C%s' % (r, c),
                      borderwidth=1).grid(row=r, column=c)

        # column : The column to put widget in; default 0 (leftmost column).
        #
        # columnspan: How many columns widgetoccupies; default 1.
        #
        # ipadx, ipady :How many pixels to pad widget, horizontally and
        # vertically, inside widget's borders.
        #
        # padx, pady : How many pixels to pad widget, horizontally and
        # vertically, outside v's borders.
        #
        # row: The row to put widget in; default the first row that is still
        # empty.
        #
        # rowspan : How many rowswidget occupies; default 1.
        #
        # sticky : What to do if the cell is larger than widget. By default,
        # with sticky='', widget is centered in its cell. sticky may be the
        # string concatenation of zero or more of N, E, S, W, NE, NW, SE, and
        # SW, compass directions indicating the sides and corners of the cell
        # to which widget sticks.

root.mainloop()
