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

class Memory:
    def __init__(self):
        self.pool = {}
        self.queu = []

    def showData(self):
        print(self.pool)

    def add_data(self, name, data, receiver=0):
        self.pool[name].append(data)
        self.queu.append([name, receiver])

    def updates(self):
        if self.queu != []:
            first_in_queu = self.queu[0]
            caller, receiver = first_in_queu
            print(caller, receiver)
            print(self.pool)
            self.queu.remove(first_in_queu)


#This class creates an interface. It accepts as arguments the function to be threaded
#and any argument that the function needs
class CreateInterface:
    def __init__(self, funk, memObj, *args, keep_alive=False):
        self.funk = funk
        self.args = tuple(args)
        self.keep_alive = keep_alive
        self.stop_signal = threading.Event()    #Signal to stop the thread
        stop_signals.append(self.stop_signal)
        self.results = []
        self.read = 0
        self.memObj = memObj
        self.iden = funk.__name__
        self.memObj.pool.update({self.iden:[]})

    #Start the interface. It will pass the stopping signal as the first argument
    def startInterface(self):
        executor = cf.ThreadPoolExecutor(max_workers=1, thread_name_prefix=f'cortex-{self.iden}')
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
            self.memObj.add_data(self.iden, output)

        if self.keep_alive and not self.stop_signal.is_set():
            self.startInterface()
            
    #Set the signal to stop the thread
    def stopInterface(self):
        self.stop_signal.set()

    def wait(self): #TODO Add timeout
        # while not self.thread.done() and self.read == len(self.results):
        while self.read == len(self.results):
            if self.stop_signal.is_set():
                return None
            pass
        
        self.read += 1
        return self.results[-1]
        
#This function has to be called to keep the main thread alive.
#It will stop the loop when Ctrl+C is pressed or when there are no threads running
def keepRunning():
    while True:
        sleep(1)
        logging.debug(f"Total number of threads: {threading.active_count()}")
        logging.debug(f"{threading.enumerate()}")
        
        if threading.active_count() == 1:
            print('out')
            break

if __name__ == '__main__':
    #Import testing functions
    from tests.test_funk import *

    light = Light()
    mic = Mic()

    # #Create the interfaces
    mem = Memory()

    voice = CreateInterface(mic.listening, mem, keep_alive=True)
    shining = CreateInterface(light.shine, mem)

    # #Start them
    voice.startInterface()
    # sleep(1)
    # shining.startInterface()

    # sleep(3)
    mic.command = 1

    voice_command = voice.wait()
    # light.state = voice_command
    sleep(1)
    mic.command = 0
    voice_command = voice.wait()
    # light.state = voice_command

    # # sleep(1)
    # # #Destroy nombre interface
    # # nombre.stopInterface()

    # #Keep the main loop running to be able to stop edad by pressing Ctrl+C
    # keepRunning()

    
    #Testing Memory class
    # mem = Memory()

    # writer = Writer(mem, "w")
    # writer.write("there")
    # writer.write("asd")
    mem.showData()
    keepRunning()


