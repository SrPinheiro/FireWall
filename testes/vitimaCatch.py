#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

grab = Motor(Port.C)
ultraSonic =  UltrasonicSensor(Port.S3)
ev3 = EV3Brick()

m1 = Motor(Port.B)
m2 = Motor(Port.A)

m = DriveBase(m1, m2, 35, 210)
motor = DriveBase(left_motor=m1, right_motor=m2, wheel_diameter=35, axle_track=210)


m1.run(20)
m2.run(-20)

upDistance = 0
lastDistance = 0

while True:
    distance = ultraSonic.distance()
    if (distance < lastDistance * 0.8):
        m1.stop()
        m2.stop()
        wait(100)
        
        motor.turn(20)
        
        dr = ultraSonic.distance()
        
        motor.turn(-20)
        motor.turn(-20)
        
        dl = ultraSonic.distance()
        
        motor.turn(20)
    
        if dr > distance * 1.2 and dl > distance * 1.2:
            while True:
                ev3.speaker.beep()
                wait(200)
        
        
    
    else:
        lastDistance = distance
        
        
    
    ev3.screen.clear()
    ev3.screen.print(distance)
    
    
    