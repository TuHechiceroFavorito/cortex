from time import sleep
import concurrent.futures as cf
import threading
import signal
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

exit_event = threading.Event()
stop_signals = []

def safe_stop(signum, frame):
    for stop_signal in stop_signals:
        stop_signal.set()

    exit_event.set()

signal.signal(signal.SIGINT, safe_stop)


class CreateInterface:
    def __init__(self, funk, *args):
        self.funk = funk
        self.args = tuple(args)
        self.stop_signal = threading.Event()
        stop_signals.append(self.stop_signal)

    def startInterface(self):
        executor = cf.ThreadPoolExecutor(max_workers=1, thread_name_prefix='cortex')
        thread = executor.submit(self.funk, self.stop_signal, *self.args)
        executor.submit(self.error_handler, thread)
        self.thread = thread

    def error_handler(self, thread):
        result = thread.exception()

        if result != None:
            print(result)

    def stopInterface(self):
        self.stop_signal.set()
        

def keepRunning():
    while True:
        sleep(1)
        logging.debug(f"Total number of threads: {threading.enumerate()}")
        logging.debug(f"{len(threading.enumerate())}")
        if exit_event.is_set():
            print('out')
            break
        
        elif len(threading.enumerate()) == 1:
            break

if __name__ == '__main__':
    from tests.test_funk import *

    nombre = CreateInterface(name, "Kierot")
    edad = CreateInterface(age)

    nombre.startInterface()
    sleep(1)
    edad.startInterface()

    sleep(1)
    nombre.stopInterface()
    keepRunning()