from time import sleep
import concurrent.futures as cf

from tests.test_funk import *

class CreateInterface:
    def __init__(self, funk, *args):
        self.funk = funk
        self.args = list(args)

    def startInterface(self):
        executor = cf.ThreadPoolExecutor()

        thread = executor.submit(self.funk)
        executor.submit(self.error_handler, thread)

    def error_handler(self, thread):
        result = thread.exception()
        if result != None:
            print(result)
    
nombre = CreateInterface(name)
edad = CreateInterface(age)

nombre.startInterface()
edad.startInterface()

sleep(5)

print('not done yet')