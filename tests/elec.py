import threading

class Led:
    def __init__(self):
        self.estado = None

    def ton(self):
        self.estado = "on"

    def toff(self):
        self.estado = "off"

class sensor:
    def __init__(self):
        self.distance = None

    def __read(self): #Returns the distance the sensor reads
        resistance = None
        dist_analog = 2/1023 * resistance
        if dist_analog > 1023:
            dist_analog = 1023

        return dist_analog

if __name__ == '__main__':
    l1 = Led()

    l1.ton()

    print(l1.estado)