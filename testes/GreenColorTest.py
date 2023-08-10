#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from colorCheck import ColorCheck
from devices import Devices

ev3 = EV3Brick()
ev3.speaker.beep()

def rgbCheck():
    # ev3.speaker.beep()
    color2 = Devices.RColorSensor.rgb()
    
    ev3.screen.clear()
    ev3.screen.print("R: " + str(color2[0]))
    ev3.screen.print("G: " + str(color2[1]))
    ev3.screen.print("B: " + str(color2[2]))
    wait(500)
    
    ev3.screen.clear()
    ev3.screen.print("C: " + str(Devices.RColorSensor.color()))
    ev3.screen.print("A: " + str(Devices.RColorSensor.ambient()))
    ev3.screen.print("R: " + str(Devices.RColorSensor.reflection()))
    wait(500)
    
if __name__ == "__main__":
    while True:
        rgbCheck()
    