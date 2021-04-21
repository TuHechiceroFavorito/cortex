

class Leds:
    def __init__(self):
        self.estado = 0

    def ton(self):
        self.estado = 1

    def toff(self):
        self.estado = 0


l1 = Leds()

l1.ton()

print(l1.estado)