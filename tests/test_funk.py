from time import sleep
import threading
from linker import *


def name(stop_signal, name='asd'):
    for i in range(500):
        safeprint(f'My name is {name}')
        sleep(2)

        if stop_signal.is_set():
            safeprint('name out')
            break


def age(stop_signal, age=0):
    for i in range(500):
        safeprint(f"I'm {age} years old")
        sleep(2)

        if stop_signal.is_set():
            safeprint('age out')
            break
