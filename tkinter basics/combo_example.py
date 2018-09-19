from tkinter import *
from tkinter import ttk
#primary window
tkwindow = Tk()

#combo box
cbox = ttk.Combobox(tkwindow, values=[1,2,3], state='readonly')
cbox.pack()

#label
lbl=Label(tkwindow,text='')
lbl.pack()

def printit(*args): #change the label to current value of combobox
    cbox.selection_clear()
    lbl.config(text=cbox.get())


cbox.bind("<<ComboboxSelected>>", printit)
tkwindow.mainloop()