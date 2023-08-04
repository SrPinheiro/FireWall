#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    UltrasonicSensor,
    GyroSensor,
)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
motor = DriveBase(
    left_motor=Motor(Port.B),
    right_motor=Motor(Port.A),
    wheel_diameter=35,
    axle_track=210,
)

ev3.speaker.beep()

while True:
    if Button.LEFT in ev3.buttons.pressed():
        motor.turn(-90)

    elif Button.RIGHT in ev3.buttons.pressed():
        motor.turn(90)

    elif Button.DOWN in ev3.buttons.pressed():
        motor.turn(180)

    elif Button.UP in ev3.buttons.pressed():
        motor.turn(360)

    wait(400)
