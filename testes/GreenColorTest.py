#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from colorCheck import ColorCheck


sensorL = ColorSensor(Port.S1)
ev3 = EV3Brick()
ev3.speaker.beep()

def rgbCheck():
    # ev3.speaker.beep()
    color2 = sensorL.rgb()
    
    ev3.screen.clear()
    ev3.screen.print("R: " + str(color2[0]))
    ev3.screen.print("G: " + str(color2[1]))
    ev3.screen.print("B: " + str(color2[2]))
    wait(500)

def colorCheck():
    CNAME = ColorCheck.check(sensorL)

    ev3.screen.clear()
    ev3.screen.print(CNAME)
    ev3.screen.print(sensorL.reflection())
    wait(500)
    

while True:
    colorCheck()
    rgbCheck()
    
    