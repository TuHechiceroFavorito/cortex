from time import sleep
import concurrent.futures as cf

def name(name='asd'):
    for i in range(5):
        print(f'My name is {name}')
        sleep(2)

def age(age=0):
    for i in range(5):
        print(f"I'm {age} years old")
        sleep(2)

class CreateInterface:
    def __init__(self, funk, *args):
        self.funk = funk
        self.args = list(args)

    def startInterface(self):
        executor = cf.ThreadPoolExecutor()
        executor.submit(self.funk)

nombre = CreateInterface(name)
edad = CreateInterface(age)

nombre.startInterface()
edad.startInterface()

sleep(5)

print('not done yet')