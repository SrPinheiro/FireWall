#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# from lineFollower import seguir_linha


    

try:
    ev3 = EV3Brick()
    ev3.speaker.beep()
    
    motor_direito = Motor(Port.A)
    motor_esquerdo = Motor(Port.B)
    robot = DriveBase(motor_esquerdo, motor_direito, wheel_diameter=55.5, axle_track=104)
    
    sensor_cor_direito = ColorSensor(Port.S1)
    sensor_cor_esquerdo = ColorSensor(Port.S2)
    
    maxSpeed = 100
    normalSpeed = 100
    turnSpeed = 200
    turnAngle = 100
    minSpeed = 50

    
    
    while True:
        leftReflection = int(sensor_cor_esquerdo.reflection())
        rightReflection = int(sensor_cor_direito.reflection())
        
        leftColor = sensor_cor_esquerdo.color()
        rightColor = sensor_cor_direito.color()
        
        ev3.screen.clear()
        ev3.screen.print(rightReflection, leftReflection)
        
        if(leftColor == Color.GREEN and rightColor == Color.GREEN):
            robot.drive(200, 0)
        
        elif(leftColor == Color.GREEN and rightColor != Color.GREEN):
            robot.drive(200, turnAngle * -1)
        
        elif(leftColor != Color.GREEN and rightColor == Color.GREEN):
            robot.drive(200, turnAngle)
        
        if(rightReflection < 40 and leftReflection < 40):
            robot.drive(maxSpeed, 0)
        
        elif(rightReflection < 40):
            robot.drive(maxSpeed, turnAngle)
        
        elif(leftReflection < 40):
            robot.drive(maxSpeed, turnAngle * -1)
        
        elif(leftReflection > 40 and rightReflection > 40):
            robot.drive(maxSpeed, 0)
            
        wait(2)
        
        

    # sensor_cor_esquerdo = ColorSensor(Port.S1)
    # sensor_cor_direito = ColorSensor(Port.S2)

    # seguir_linha(robot, sensor_cor_esquerdo, sensor_cor_direito, ev3)
    ev3.screen.clear()
    ev3.screen.print('fechou')
    wait(2000)

except Exception as e:
    ev3.screen.clear()
    ev3.screen.print(e)
    robot.stop()
    wait(10000)
