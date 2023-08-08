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
        Devices.motor.drive(45, 0)
        self.LgreenMap = 0
        self.RgreenMap = 0
        
        self.LWhiteMap = 0
        self.RWhiteMap = 0
        
        self.LBlackMap = 0
        self.RBlackMap = 0
        
        self.run()
        
    def turnar(self):
        Devices.motor.stop()
        Devices.motor.turn(180)
        
        while True:
            Devices.brain.speaker.beep()
            wait(500)
        
    def run(self):
        while True:
            cor1 = ColorCheck.check(Devices.RColorSensor)
            cor2 = ColorCheck.check(Devices.LColorSensor)
            
            self.setState(cor1, "R")
            self.setState(cor2, "L")
            
            if cor1 == Color.WHITE or cor2 == Color.WHITE:
                if(self.LgreenMap >= 5 or self.RgreenMap >= 5):
                    self.turnar()
            
            Devices.brain.screen.clear()
            Devices.brain.screen.print(cor1)
            Devices.brain.screen.print(cor2)
            Devices.brain.screen.print(self.LgreenMap)
            Devices.brain.screen.print(self.RgreenMap)
        
    def setState(self, throwler, sensor):
        if throwler == Color.WHITE:
            if sensor == "L":
                self.LWhiteMap += 1
                self.LBlackMap = 0
                self.LgreenMap = 0
            elif sensor == "R":
                self.RWhiteMap += 1
                self.RBlackMap = 0
                self.RgreenMap = 0
                
        elif throwler == Color.BLACK:
            if sensor == "L":
                self.LWhiteMap = 0
                self.LBlackMap += 1
                self.LgreenMap = 0
            elif sensor == "R":
                self.RWhiteMap = 0
                self.RBlackMap += 1
                self.RgreenMap = 0
                
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