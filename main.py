#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from lineFollower import seguir_linha

ev3 = EV3Brick()

motor_esquerdo = Motor(Port.B)
motor_direito = Motor(Port.C)
drive_base = DriveBase(motor_esquerdo, motor_direito, wheel_diameter=55.5, axle_track=104)

sensor_cor_esquerdo = ColorSensor(Port.S1)
sensor_cor_direito = ColorSensor(Port.S2)

try:
    seguir_linha(drive_base, sensor_cor_esquerdo, sensor_cor_direito, ev3)
except Exception as e:
    ev3.screen.clear()
    ev3.screen.print(e)
    drive_base.stop()
