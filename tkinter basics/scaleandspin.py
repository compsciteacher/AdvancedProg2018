from tkinter import *
import random
import time
root = Tk()

class App:

    def __init__(self, master):
        mframe = Frame(master)
        mframe.pack()

        master.title("Final Basic Widgets")

        self.scval = IntVar()
        self.scval.set(1)

        self.spinval =IntVar()
        self.spinval.set(1)

        self.sc = Scale(mframe, from_=1, to_=(random.randint(1, 500)), orient=HORIZONTAL, command=self.scvalchange)
        self.sc.grid(column=0, row=0)

        self.sp = Spinbox(mframe, from_=1, to_=10, command=self.labelupdate)
        self.sp.grid(column=0, row=1)

        self.l = Label(mframe, text=("Value: %d" % self.spinval.get()))
        self.l.grid(column=0, row=2)

        self.ok = Button(mframe, text="OK", command=self.yaywindow)
        self.ok.grid(column=0, row=3)

        self.close = Button(mframe, text="CLOSE", command=root.destroy)
        self.close.grid(column=0, row=4)

    def scvalchange(self, x):
        self.scval.set(x)
    def labelupdate(self):
        self.spinval.set(self.sp.get())
        self.l.config(text=("Value: %d" % self.spinval.get()))
    def yaywindow(self):
        for x in range(self.scval.get()):
            top = Toplevel()
            top.geometry('%sx%s' % (random.randint(200, 800), random.randint(200, 800)))
            top.title("Yay!")
            for x in range(random.randint(20, 100)):
                z=random.randint(1,100)
                y=random.randint(1,100)
                msg = Message(top, text="Yay!")
                msg.grid(column=z, row=y)
            button = Button(top, text="CLOSE", command=top.destroy)
            button.grid(column=101, row=101)





app = App(root)
root.geometry('200x150')
root.mainloop()