import tkinter as tk
import sys, os
from PIL import Image, ImageTk

#Quick fix for an import issue. Will be improved to a better solution later on
if os.environ.get("kierot") == "True":
    sys.path.append(os.getcwd())
else:
    sys.path.append(os.path.abspath(os.path.join('..', 'elec')))

from tests.elec import *
from tests import tg
from linker import *

class Application(tk.Frame):
    led = Led()

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.widgets()

    def widgets(self):

        self.result = tk.Label(root)
        self.result.pack()

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

        self.print_state = tk.Button(self)
        self.print_state["text"] = "LED state"
        self.print_state["command"] = self.print
        self.print_state.pack(side="top")

    def ton(self):
        self.led.ton()
        self.result["image"] = ledon

    def toff(self):
        self.led.toff()
        self.result["image"] = ledoff

    def print(self):
        print(self.led.estado)


root = tk.Tk()

try:
    root.iconbitmap("diamond.ico")
except:
    print("No image found")

root.title("Interface for fucking retarded noobs")
root.geometry("512x512")

ledoff = Image.open("ledoff.png")
ledon = Image.open("ledpng.png")

ledoff = ledoff.resize((200,200), Image.ANTIALIAS)
ledon = ledon.resize((200,200), Image.ANTIALIAS)

ledoff = ImageTk.PhotoImage(image=ledoff)
ledon = ImageTk.PhotoImage(image=ledon)

app = Application(master=root)
frame = tk.Frame(root, width=200, height=200)
frame.pack()

bot = CreateInterface(tg.main)
bot.startInterface()
app.mainloop()