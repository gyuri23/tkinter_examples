#!/usr/bin/python
import tkinter

main_window = tkinter.Tk()      # http://effbot.org/tkinterbook/wm.htm
main_window.title('Ablak neve')
main_window.geometry('300x500+500+100') #széles x magas + bal elűről jobbra + bal felűről lefelé

left_frame = tkinter.Frame(main_window, bg='green')
left_frame.pack(side='right')
left_frame.place(rely=0.8)

tkinter.Label(left_frame, text='Label').grid(row=0, column=0)
tkinter.Label(left_frame, text=' xxxx').grid(row=0, column=1)
tkinter.Label(left_frame, text='La').grid(row=1, column=0, sticky='w')
tkinter.Label(left_frame, text=' xfgfgxx').grid(row=1, column=1)

var = tkinter.StringVar()
label = tkinter.Message(main_window, textvariable=var, relief='raised')
var.set("Hey!? How are you doing?")
label.pack()


#msg = tkinter.Message(main_window, anchor='w', width=80, justify='left', bg='blue', text='szöveg')
msg = tkinter.Message(main_window, bg='brown', pady=20, text='1234567890')
msg.pack()
msg.place(#rely=0.2
          #relheight=0.2,
          #relwidth=0.6,
          #anchor='s'
          #x=10
          )

msg2 = tkinter.Message(main_window, bg='blue', text='1234567890')
msg2.pack()
msg2.place(rely=0.4
          #relheight=0.2,
          #relwidth=0.6,
          #anchor='s'
          #x=10
          )



main_window.mainloop()