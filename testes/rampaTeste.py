#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

motor = Motor(Port.C)

def upGrab():
    motor.run_until_stalled(200, 0)
        
def downGrab():
    motor.run_until_stalled(-200, 0)

while True:
    if Button.UP in ev3.buttons.pressed():
        ev3.speaker.beep()
        upGrab()
        
    elif Button.DOWN in ev3.buttons.pressed():
        ev3.speaker.beep()
        downGrab()
    
    wait(200)
    