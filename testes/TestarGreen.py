#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from devices import Devices
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from colorCheck import ColorCheck

class teste():
    def __init__(self):
        self.LgreenMap = 0
        self.RgreenMap = 0
        
        self.LWhiteMap = 0
        self.RWhiteMap = 0
        
        self.LBlackMap = 0
        self.RBlackMap = 0
        
        self.andar = False
        
        self.run()
    
        
    def run(self):
        while True:
            cor1 = ColorCheck.check(Devices.RColorSensor)
            
            if Devices.brain.buttons.pressed():
                self.andar = not self.andar
                
            # if andar:
            #     Devices.motor.drive(30, 0)
                
            # else:
            #     Devices.motor.stop()
            
            self.setState(cor1, "R")
            
            if self.RBlackMap >= 10:
                self.RgreenMap = 0
            
            Devices.brain.screen.clear()
            Devices.brain.screen.print(cor1)
            Devices.brain.screen.print(self.RgreenMap)
        
    def setState(self, throwler, sensor):
        if throwler == Color.WHITE:
            if sensor == "L":
                self.LWhiteMap += 1
                self.LBlackMap = 0
                #self.LgreenMap = 0
            elif sensor == "R":
                self.RWhiteMap += 1
                self.RBlackMap = 0
                #self.RgreenMap = 0
                
        elif throwler == Color.BLACK:
            if sensor == "L":
                self.LWhiteMap = 0
                self.LBlackMap += 1
                self.LgreenMap = 0
            elif sensor == "R":
                self.RWhiteMap = 0
                self.RBlackMap += 1
                #self.RgreenMap = 0
                
        elif throwler == Color.GREEN:
            if sensor == "L":
                self.LWhiteMap = 0
                self.LBlackMap = 0
                self.LgreenMap += 1
            elif sensor == "R":
                self.RWhiteMap = 0
                self.RBlackMap = 0
                self.RgreenMap += 1

teste()