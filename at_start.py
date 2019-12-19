import time
import tkinter
import at, atg

def a():
    atg.gui()
    wind.destroy()

def b():
    at.at()
    wind.destroy()

wind = tkinter.Tk()
fr1 = tkinter.Frame(wind, relief = "sunken", borderwidth = 5)
bt_gui = tkinter.Button(fr1, text = "GUI", command = a)
bt_at = tkinter.Button(fr1, text = "AT(shell)", command = b)
fr1.pack()
bt_gui.pack()
bt_at.pack()

wind.mainloop()
