from time import sleep
import concurrent.futures as cf

class CreateInterface:
    def __init__(self, funk, *args):
        self.funk = funk
        self.args = list(args)

    def startInterface(self):
        executor = cf.ThreadPoolExecutor()
        thread = executor.submit(self.funk, *self.args)
        executor.submit(self.error_handler, thread)

    def error_handler(self, thread):
        result = thread.exception()

        if result != None:
            print(result)
    

if __name__ == '__main__':
    from tests.test_funk import *

    nombre = CreateInterface(name, "Kierot")
    edad = CreateInterface(age)

    nombre.startInterface()
    # edad.startInterface()

    # sleep(5)

    print('not done yet')