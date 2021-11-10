from time import sleep
import threading
from multiprocessing import Lock
import signal
import logging

logger = logging.getLogger(__name__)

logger.addHandler(logging.NullHandler())

#Signal to stop everything on Ctrl+C
exit_event = threading.Event()

#Lock for to print every print in a single line
lock = Lock()

#This class creates an interface. It accepts as arguments the function to be threaded
#and any argument that the function needs
#If signals is set to True, it will create a signal for the interface to allow it to be stopped
#manually
class CreateInterface:
    def __init__(self, funk, *args, signals=False):
        self.funk = funk
        self.args = list(args)
        self.signals = signals
        self.buildArgs()
        safelogging('debug', f"Interface for '{self.funk.__name__}' created")

    #Build arguments. Now there are 1, but if the list grows this function is going to be useful
    #The order of the arguments in the current version is stop_signal, *args
    def buildArgs(self):
        args = []

        #If signal is supplied, add a signal to the arguments to pass to the function
        if self.signals:
            self.stop_signal = threading.Event()    #Signal to stop the thread
            args.append(self.stop_signal)

        args += self.args
        self.args = args

    #Start the interface. It will pass the stopping signal as the first argument
    #In this version, I'm using threading instead of concurrent futures. Allows for daemon
    #which automates stopping with ctrl + c
    def startInterface(self):
        thread = threading.Thread(target=self.funk, name=f'cortex-{self.funk.__name__}', args=[*self.args])
        thread.setDaemon(True)
        thread.start()
        safelogging('debug', f"Thread from '{self.funk.__name__}' created")

    #Set the signal to stop the thread
    def stopInterface(self):
        self.stop_signal.set()
        safelogging('debug', f"Thread from '{self.funk.__name__}' stopped")

#This ensures that the text is printed in a new line and doesn't mix with other threads prints
def safeprint(text):
    lock.acquire()
    try:
        print(text)
    finally:
        lock.release()

#Same as safeprint but for logging. Sometimes it still prints where it shouldnt
#TODO Check that eval behaves as print in this situation
def safelogging(level, text):
    lock.acquire()
    try:
        eval(f'logger.{level}("{text}")')
    finally:
        lock.release()

#Stop everything
def safe_stop(signum=None, frame=None):
    exit_event.set()
        
#This function has to be called to keep the main thread alive.
#It will stop the loop when Ctrl+C is pressed or when there are no threads running
def keepRunning():
    #Set the signal for Ctrl+C
    signal.signal(signal.SIGINT, safe_stop)

    while True:
        sleep(1)
        logging.debug(f"Total number of threads: {threading.active_count()}")
        logging.debug(f"{len(threading.enumerate())}")

        #Currently not working
        #TODO Make sure that the signal works propertly
        if exit_event.is_set():
            logger.info('Stopping...')
            break

        if threading.active_count() == 1:
            logger.info('Program ended running')
            break

if __name__ == '__main__':
    #Import testing functions
    from tests.test_funk import *

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

    #Create the interfaces
    nombre = CreateInterface(name, "Kierot", signals=True)
    nombre.startInterface()

    edad = CreateInterface(age, signals=True)
    edad.startInterface()

    sleep(5)

    #Stop nombre
    nombre.stopInterface()

    #Keep the main loop running to be able to stop edad by pressing Ctrl+C
    keepRunning()