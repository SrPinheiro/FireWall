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
        LReflection = sensor_cor_esquerdo.reflection()
        RReflection = sensor_cor_direito.reflection()
        LColor = sensor_cor_esquerdo.color()
        RColor = sensor_cor_direito.color()
        LAmbient = sensor_cor_esquerdo.ambient()
        RAmbient = sensor_cor_direito.ambient()
        RRGB = sensor_cor_direito.rgb()
        LRGG = sensor_cor_esquerdo.rgb()
        
        ev3.screen.clear()
        ev3.screen.print(RReflection + " - " + LReflection)
        ev3.screen.print(RColor)
        ev3.screen.print(LColor)
        
        wait(3000)
        ev3.screen.clear()
        ev3.screen.print(LAmbient + " - " + RAmbient)
        ev3.screen.print(RRGB)
        ev3.screen.print(LRGG)
        
        wait(3000)
    
except Exception as err:
    ev3.screen.print(err)
    wait(10000)