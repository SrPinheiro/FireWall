#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
ultraSonic = UltrasonicSensor(Port.S3)

while True:
    distance = ultraSonic.distance()

    ev3.screen.clear()
    ev3.screen.print(distance)
    
    if distance <= 50:
        ev3.speaker.beep()
        ev3.screen.print("!MUITO PERTO!")
    elif(distance <= 100):
        ev3.screen.print("!PERTO!")
    else:
        ev3.screen.print("longe")
    wait(100)
