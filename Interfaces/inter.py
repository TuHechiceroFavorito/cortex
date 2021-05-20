import tkinter as tk
import sys, os
from PIL import Image, ImageTk

#Quick fix for an import issue. Will be improved to a better solution later on
if os.environ.get("kierot") == "True":
    sys.path.append(os.getcwd())
else:
    sys.path.append(os.path.abspath(os.path.join('..', 'elec')))

from tests.elec import *

class Application(tk.Frame):
    led = Led()
    ir = sensor()

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.preferences()
        self.widgets()

    def preferences(self):
        try:
            self.master.iconbitmap("diamond.ico")
        except:
            print("No image found")

        self.master.title("Interface for fucking retarded noobs")
        root.geometry("270x370")

    def widgets(self):
        self.turn_on = tk.Button(self)
        self.turn_on["text"] = "Turn on the LED"
        self.turn_on["command"] = self.ton
        self.turn_on.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.turn_off = tk.Button(self)
        self.turn_off["text"] = "Turn off the LED"
        self.turn_off["command"] = self.toff
        self.turn_off.pack(side="top")

        self.distance = tk.Scale(self, variable=self.ir.dist, from_=0.0, to=2.0, resolution=0.01, orient=tk.HORIZONTAL)
        self.distance.pack(side="top")
        
        self.dist_label = tk.Label(self, text="Distance of the object to the IR sensor in metres")
        self.dist_label.pack(side="top")

        ledoff = Image.open("ledoff.png")
        ledon = Image.open("ledpng.png")

        ledoff = ledoff.resize((200,200), Image.ANTIALIAS)
        ledon = ledon.resize((200,200), Image.ANTIALIAS)

        self.ledoff = ImageTk.PhotoImage(image=ledoff)
        self.ledon = ImageTk.PhotoImage(image=ledon)

        self.result = tk.Label(self, image=self.ledoff)
        self.result.pack()

    def ton(self):
        self.led.ton()
        self.result["image"] = self.ledon

    def toff(self):
        self.led.toff()
        self.result["image"] = self.ledoff

    def print(self):
        print(self.led.estado)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()