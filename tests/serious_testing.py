import os, sys
from time import sleep
sys.path.append(os.getcwd())

import linker
from test_funk import *
import tg

#This would be the nucleus of the code
#It controls an led that can be controled by a microphone
#and with a tg interface

mem = Memory()

mic = Mic()
light = Light()

led = linker.CreateInterface(light.shine, mem)
voice = linker.CreateInterface(mic.listening, mem, keep_alive=True)

led.startInterface()
voice.startInterface()

sleep(2)
mic.command = 1

light.state = voice.wait()
sleep(2)
mic.command = 0
light.state = voice.wait()
# linker.keepRunning()
while True:
    mem.updates()


# i = 0
# while True:
#     sleep(3)
#     i += 1
#     print(i % 2)
#     mic.command = i % 2
#     light.state = voice.wait()
