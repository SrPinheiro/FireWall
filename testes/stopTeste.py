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

motor = DriveBase(left_motor=Motor(Port.B), right_motor=Motor(Port.A), wheel_diameter=32.5, axle_track=180)

ev3 = EV3Brick()
ev3.speaker.beep()
ev3.screen.clear()


while True:
    ev3.screen.clear()
    ev3.screen.draw_text(50, 60, "Teste de freio")
    ev3.screen.draw_text(50, 80, "Freio STOP")
    while not ev3.buttons.pressed():
        wait(100)
    
    motor.drive(250, 0)
    
    wait(1000)
    motor.stop()
    ev3.spaker.beep(duration=2000)
    
    ev3.screen.clear()
    ev3.screen.draw_text(50, 60, "Teste de freio")
    ev3.screen.draw_text(50, 80, "Freio brake")
    while not ev3.buttons.pressed():
        wait(100)
    
    motor.drive(250, 0)
    
    wait(1000)
    motor.brake()
    ev3.spaker.beep(duration=2000)
    
    ev3.screen.clear()
    ev3.screen.draw_text(50, 60, "Teste de freio")
    ev3.screen.draw_text(50, 80, "Freio hold")
    while not ev3.buttons.pressed():
        wait(100)
    
    motor.drive(250, 0)
    
    wait(1000)
    motor.hold()
    ev3.spaker.beep(duration=2000)
    
    