

class Led:
    def __init__(self):
        self.estado = 0

    def ton(self):
        self.estado = 1

    def toff(self):
        self.estado = 0

if __name__ == '__name__':
    l1 = Led()

    l1.ton()

    print(l1.estado)

class sensor:
    def __init__(self):
        self.deteccion = 0

    def detectar(self):
        self.deteccion = 1 #Aquí que llegue un comando que sea generado por la detección física
        self.marcar()
        self.deteccion = 0 #Asumo que buscamos un pulso no un switch

    def marcar(self):

        return(self.deteccion)