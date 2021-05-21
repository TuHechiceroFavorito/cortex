from time import sleep
import concurrent.futures as cf
import threading
import signal
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


#Signal to stop everything on Ctrl+C
exit_event = threading.Event()
#Store all stopping signals for every new thread created
stop_signals = []

#Stop everything
def safe_stop(signum=None, frame=None):
    for stop_signal in stop_signals:
        stop_signal.set()

    exit_event.set()

#Set the signal for Ctrl+C
signal.signal(signal.SIGINT, safe_stop)

#This class creates an interface. It accepts as arguments the function to be threaded
#and any argument that the function needs
class CreateInterface:
    def __init__(self, funk, *args):
        self.funk = funk
        self.args = tuple(args)
        self.stop_signal = threading.Event()    #Signal to stop the thread
        stop_signals.append(self.stop_signal)
        self.results = []

    #Start the interface. It will pass the stopping signal as the first argument
    def startInterface(self):
        executor = cf.ThreadPoolExecutor(max_workers=1, thread_name_prefix='cortex')
        thread = executor.submit(self.funk, self.stop_signal, *self.args)
        executor.submit(self.error_handler, thread)
        executor.submit(self.output_handler, thread)
        self.thread = thread

    #This function handles errors of the functions
    #It is threaded to avoid the program to wait for the thread to be completed
    def error_handler(self, thread):
        error = thread.exception()

        if error != None:
            logging.error(error)

    def output_handler(self, thread):
        output = thread.result()

        if output != None:
            self.results.append(output)
            
    #Set the signal to stop the thread
    def stopInterface(self):
        self.stop_signal.set()
        
#This function has to be called to keep the main thread alive.
#It will stop the loop when Ctrl+C is pressed or when there are no threads running
def keepRunning():
    while True:
        sleep(1)
        logging.debug(f"Total number of threads: {threading.enumerate()}")
        logging.debug(f"{len(threading.enumerate())}")
        
        if len(threading.enumerate()) == 1:
            print('out')
            break

if __name__ == '__main__':
    #Import testing functions
    from tests.test_funk import *

    light = Light()
    mic = Mic()

    #Create the interfaces
    voice = CreateInterface(mic.listening)
    shining = CreateInterface(light.shine)

    #Start them
    voice.startInterface()
    sleep(1)
    shining.startInterface()

    sleep(3)
    mic.command = 1
    
    while len(voice.results) == 0:
        pass

    voice_command = voice.results[-1]
    light.state = voice_command
    sleep(1)
    mic.command = 0

    # sleep(1)
    # #Destroy nombre interface
    # nombre.stopInterface()

    #Keep the main loop running to be able to stop edad by pressing Ctrl+C
    keepRunning()