from time import sleep

#This simulates an LED
class Led:
    def __init__(self):
        self.estado = None

    def ton(self):
        self.estado = "on"

    def toff(self):
        self.estado = "off"

#This simulates an ir sensor with a range of 2m
class sensor:
    def __init__(self, light=1023):
        self.distance = None
        self.dist = light

    def read(self): #Returns the signal the sensor reads
        dist_analog = 1023/2 * self.dist
        if dist_analog > 1023:
            dist_analog = 1023

        return dist_analog

if __name__ == '__main__':
    #Testing led
    l1 = Led()
    l1.ton()
    print(l1.estado)
    #Testing sensor
    s = sensor()
    print(s.read())

    #Setting the distance to 1.5m
    s.dist = 1.5
    print(s.read())

    #Small test combining led and sensor
    def arduino_logic(sensor, led):
        if sensor.read() > 500:
            led.ton()
        else:
            led.toff()
        
    while True:
        s.dist = 0.2
        arduino_logic(s, l1)
        print(l1.estado)
        s.dist = 1.5
        sleep(1)
        arduino_logic(s, l1)
        print(l1.estado)
        sleep(1)
