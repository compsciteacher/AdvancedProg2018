from tkinter import *

class App: #main class that will create content

    def __init__(self, master):

        frame_r = Frame(master,width=100,height=100) #define frame
        frame_r.pack_propagate(0) #makes it so frame doesn't shrink
        frame_r.pack() #packs frame center
        self.button_r = Button(
            frame_r, text="BLUE", fg="blue", bg="red", command=self.red
            )
        self.button_r.pack(fill=BOTH,expand=1)

        frame_b = Frame(master, width=100, height=100)
        frame_b.pack_propagate(0)
        frame_b.pack()
        self.button_b = Button(frame_b, text="RED", fg="red",bg="BLUE",command=self.blue)
        self.button_b.pack(fill=BOTH,expand=1)

    def red(self):
        print('Red button!')
        


    def blue(self):
        print ("Blue button!")

root = Tk()

app = App(root)
root.title("The colored buttons window!")

root.mainloop()
root.destroy()