

class Led:
    def __init__(self):
        self.estado = 0

    def ton(self):
        self.estado = 1

    def toff(self):
        self.estado = 0

if __name__ == '__name__':
    l1 = Leds()

    l1.ton()

    print(l1.estado)