from time import sleep
import threading
from linker import *


def name(stop_signal, name='asd'):
    for i in range(500):
        print(f'My name is {name}')
        sleep(2)

        if stop_signal.is_set():
            print('name out')
            break


def age(stop_signal, age=0):
    for i in range(500):
        print(f"I'm {age} years old")
        sleep(2)

        if stop_signal.is_set():
            print('age out')
            break

class Mic:
    def __init__(self, command=0):
        self.command = command

    def listening(self, stop_signal):
        current_command = self.command
        while True:
            if current_command != self.command:
                if self.command == 0:
                    print("Turning light off")
                    return "off"

                else:
                    print("Turning light on")
                    return "on"

                current_command = self.command
            
            if stop_signal.is_set():
                break

class Light:
    def __init__(self, state="off"):
        self.state = state

    def shine(self, stop_signal):
        while True:
            sleep(0.5)
            if self.state == "on":
                # a = 0/0
                print("SHINING")
                
            elif self.state == "off":
                print("NOT SHINING")

            if stop_signal.is_set():
                break