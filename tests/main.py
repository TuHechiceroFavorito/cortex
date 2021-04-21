from time import sleep

from elec import Led

l1 = Led()

while True:
    print(l1.estado)
    sleep(1)
    l1.ton()
    print(l1.estado)
    sleep(1)
    l1.toff()