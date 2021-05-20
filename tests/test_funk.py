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
