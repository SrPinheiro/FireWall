#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from UtilCode.devices import Devices

class Calibrar:
    def __init__(self):
        self.minRed = 100
        self.maxRed = 0
        
        self.minGreen = 100
        self.maxGreen = 0
        
        self.minBlue = 100
        self.maxBlue = 0
    
    def run(self):
        Devices.brain.speaker.beep()
        Devices.motor.drive(10,0)
        while True:
            if Devices.brain.buttons.pressed():
                self.save()
                break
        
            rgb = Devices.RColorSensor.rgb()
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]
            
            self.minRed = min([self.minRed, red])
            self.maxRed = max([self.maxRed, red])
            
            self.minGreen = min([self.minGreen, green])
            self.maxGreen = max([self.maxGreen, green])
            
            self.minBlue = min([self.minBlue, blue])
            self.maxBlue = max([self.maxBlue, blue])
            
            
    def save(self):
        with open("green", "w") as file: 
            file.write(str(self.minRed) + "\n")
            file.write(str(self.maxRed) + "\n")
            file.write("\n")
            file.write(str(self.minGreen) + "\n")
            file.write(str(self.maxGreen) + "\n")
            file.write("\n")
            file.write(str(self.minBlue) + "\n")
            file.write(str(self.maxBlue) + "\n")
            
if __name__ == "__main__":
    calibrar = Calibrar()
    calibrar.run()