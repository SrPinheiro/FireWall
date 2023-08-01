#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

sensor_cor_direito = ColorSensor(Port.S1)
sensor_cor_esquerdo = ColorSensor(Port.S2)

ev3 = EV3Brick()

try:
    while True:
        leftReflection = int(sensor_cor_esquerdo.reflection())
        rightReflection = int(sensor_cor_direito.reflection())
        
        ev3.screen.clear()
        ev3.screen.print(rightReflection, leftReflection)
        
        wait(1000)
        
        leftColor = sensor_cor_esquerdo.color()
        rightColor = sensor_cor_direito.color()
        

        ev3.screen.clear()
        ev3.screen.print(rightColor)
        ev3.screen.print(leftColor)
        wait(500)
    
except Exception as err:
    ev3.screen.print(err)
    wait(10000)