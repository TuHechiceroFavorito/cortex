import tkinter as tk
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'elec')))
from tests.elec import *



class Application(tk.Frame):
    led = Led()
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.widgets()

    def widgets(self):

        self.turn_on = tk.Button(self)
        self.turn_on["text"] = "Turn on the LED"
        self.turn_on["command"] = self.led.ton
        self.turn_on.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")



        self.turn_off = tk.Button(self)
        self.turn_off["text"] = "Turn off the LED"
        self.turn_off["command"] = self.led.toff
        self.turn_off.pack(side="top")


root = tk.Tk()
root.iconbitmap("diamond.ico")
root.title("Interface for fucking retarded noobs")
root.geometry("512x512")
app = Application(master=root)
frame = tk.Frame(root, width=200, height=200)
frame.pack()

app.mainloop()