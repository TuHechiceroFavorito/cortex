import os, sys
from time import sleep
sys.path.append(os.getcwd())

import linker
from test_funk import *
import tg

#This would be the nucleus of the code
#It controls an led that can be controled by a microphone
#and with a tg interface

mic = Mic()
light = Light()

led = linker.CreateInterface(light.shine)
voice = linker.CreateInterface(mic.listening, keep_alive=True)
bot = linker.CreateInterface(tg.main)

led.startInterface()
voice.startInterface()

i = 0
while True:
    sleep(30)
    i += 1
    print(i % 2)
    mic.command = i % 2
    light.state = voice.wait()
