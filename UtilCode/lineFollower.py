from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

from UtilCode.colorCheck import ColorCheck
from UtilCode.greenState import GreenState

class LineFollower:
    def __init__(self):
        self.brain = EV3Brick()
        
        self.RColorSensor = ColorSensor(Port.S2)
        self.LColorSensor = ColorSensor(Port.S1)

        self.LMotor = Motor(Port.B)
        self.RMotor = Motor(Port.A)

        self.motor = DriveBase(left_motor=self.LMotor, right_motor=self.RMotor, wheel_diameter=35, axle_track=210)
        
        self.ultraSonic =  UltrasonicSensor(Port.S3)
        
        self.maxSpeed = 70
        self.normalSpeed = 60
        self.blackReflection = 30
        
        self.lineReflection = 10
        self.whiteReflection = 40

        self.brain.speaker.beep()
        self.brain.screen.clear()
        self.brain.light.on(Color.ORANGE)
        self.brain.screen.draw_text(50, 60, "! FireWall !")
        
        self.RgreenMap = 0
        self.LgreenMap = 0
        
        self.RWhiteMap = 0
        self.LWhiteMap = 0
        
        self.RBlackMap = 0
        self.LBlackMap = 0
        
        self.greenState = GreenState()

    def run(self):
        while True:
            distance = self.ultraSonic.distance()
            if (distance < 50):
                self.passObstacle()
                
            # self.checkLineOP()
            self.checkLineNew()
    
            
    def checkLineOp(self):
        RColor = ColorCheck.checkR(self.RColorSensor)
        LColor = ColorCheck.checkL(self.LColorSensor)
        
        if (LColor == Color.GREEN or RColor == Color.GREEN):
            # self.motor.stop()
            # self.greenState.run()
            self.brain.speaker.beep()
        
        if (LColor == Color.BLACK or RColor == Color.BLACK):
            self.makeTurn()
            
        self.motor.drive(self.maxSpeed, 0)
                
    def checkLineNew(self):
        R = self.RColorSensor.color()
        L = self.LColorSensor.color()
        
        rm = 0
        lm = 0
        
        self.setState(R, "R")
        self.setState(L, "L")
        
        #Controlador de linha direita
        if R == Color.WHITE:
            if self.RWhiteMap > 40:
                if self.RgreenMap > 140 and self.LgreenMap > 140:
                    self.motor.stop()
                    self.brain.speaker.beep()
                    self.greenState.run(self.RgreenMap, self.LgreenMap)
                    
                    wait(1000)
                
                self.RgreenMap = 0
                self.LgreenMap = 0

                
        elif R == Color.BLACK:
            if self.RBlackMap > 40:
                if self.RgreenMap > 140:
                    self.motor.stop()
                    self.brain.speaker.beep()
                    self.greenState.run(self.RgreenMap, self.LgreenMap)
                    
                    wait(1000)
                    
                self.RgreenMap = 0
                rm = 90

        #Controlador de linha esquerda
        if L == Color.WHITE:
            if self.LWhiteMap > 40:
                if self.RgreenMap > 140 and self.LgreenMap > 140:
                    self.motor.stop()
                    self.brain.speaker.beep()
                    self.greenState.run(self.RgreenMap, self.LgreenMap)
                    
                    wait(1000)
                
                self.RgreenMap = 0
                self.LgreenMap = 0

                
        elif L == Color.BLACK:
            if self.LBlackMap > 40:
                if self.LgreenMap > 140:
                    self.motor.stop()
                    self.brain.speaker.beep()
                    self.greenState.run(self.RgreenMap, self.LgreenMap)
                    
                    wait(1000)
                    
                self.LgreenMap = 0
                lm = 90
                
        self.motor.drive(self.normalSpeed, lm - rm)
            

        
        # if R == Color.WHITE:
        #     rm = 0
            
        #     if self.RgreenMap > 140 and self.LgreenMap > 140:
        #         self.motor.stop()
        #         self.brain.speaker.beep()
        #         self.greenState.run(self.RgreenMap, self.LgreenMap)
        #         wait(1000)
        #         self.RgreenMap = 0
        #         self.LgreenMap = 0
                
        #         return
            
        # elif R == Color.GREEN:
        #     self.RgreenMap += 1
        #     rm = 0
            
        # elif R == Color.BLACK:            
        #     if (self.RgreenMap > 140):
        #         self.motor.stop()
        #         self.brain.speaker.beep()
        #         self.greenState.run(self.RgreenMap, self.LgreenMap)
        #         # self.brain.screen.clear()
        #         # self.brain.screen.print(self.RgreenMap)
        #         # wait(5000)
        #         self.RgreenMap = 0
        #         return
        #     else:
        #         self.RgreenMap = 0
        #         rm = 100


        # if L == Color.WHITE:
        #     lm = 0
            
        #     if self.RgreenMap > 140 and self.LgreenMap > 140:
        #         self.motor.stop()
        #         self.brain.speaker.beep()
        #         self.greenState.run(self.RgreenMap, self.LgreenMap)
        #         self.motor.straight(50)
        #         wait(1000)
        #         self.RgreenMap = 0
        #         self.LgreenMap = 0
            
        # elif L == Color.GREEN:
        #     self.LgreenMap += 1
        #     lm = 0
            
        # elif L == Color.BLACK:            
        #     if (self.LgreenMap > 140):
        #         self.motor.stop()
        #         self.brain.speaker.beep()
        #         self.greenState.run(self.RgreenMap, self.LgreenMap)
        #         # self.brain.screen.clear()
        #         # self.brain.screen.print(self.RgreenMap)
        #         # wait(5000)
        #         self.LgreenMap = 0
        #         self.RgreenMap = 0
                
        #         return
        #     else:
        #         self.LgreenMap = 0
        #         lm = 100

        # self.motor.drive(self.normalSpeed, lm - rm)
            
    def makeTurn(self):        
        while True:
            R = ColorCheck.check(self.RColorSensor)
            L = ColorCheck.check(self.LColorSensor)
            
            if(R == Color.BLACK and L == Color.BLACK):
                self.motor.drive(self.normalSpeed, 0)
                
            elif(R == Color.GREEN or L == Color.GREEN):
                # self.greenState()
                "a"
                
            elif(R == Color.WHITE and L == Color.WHITE):
                break
            
            elif(R == Color.BLACK and L == Color.WHITE):
                self.motor.drive(self.normalSpeed, 95)
                
            elif (R == Color.WHITE and L == Color.BLACK):
                self.motor.drive(self.normalSpeed, -95)
                
            wait(50)
    
    def passObstacle(self):
        self.motor.stop()
        
        distance = self.ultraSonic.distance()
        
        while distance > 100:

            if (distance < 100):
                self.motor.straight((100 - distance) * -1)  
            
            distance = self.ultraSonic.distance()    
        
        self.motor.turn(-90)
        self.motor.straight(20 * 10)
        
        self.motor.turn(90)
        self.motor.straight(40 * 10)
        
        self.motor.turn(90)
        self.motor.straight(5 * 10)
        LBlack = False
        
        while True:
            self.motor.drive(self.normalSpeed, 0)
            LS = ColorCheck.check(self.LColorSensor)
            RS = ColorCheck.check(self.RColorSensor)
            
            if (LBlack and LS == Color.WHITE):
                break
            
            elif (LS == Color.BLACK):
                self.motor.drive(self.maxSpeed, 100)
                LBlack = True
                
            elif (RS == Color.BLACK):
                self.motor.stop()
                self.motor.turn(-50)
                self.motor.straight(-3 * 10)
                self.motor.drive(self.maxSpeed, -100)
                
                break
            else:
                self.motor.drive(self.normalSpeed, 0)
    
    #
    # Esse metodo serve para detectar quantas vezes uma cor foi vista em sequencia
    # Objetivo: corrigir a margem de erro do sensor de cor
    #
    def setState(self, throwler, sensor):
        if throwler == Color.WHITE:
            if sensor == "L":
                self.LWhiteMap += 1
                self.LBlackMap = 0
                # self.LgreenMap = 0
            elif sensor == "R":
                self.RWhiteMap += 1
                self.RBlackMap = 0
                # self.RgreenMap = 0
                
        elif throwler == Color.BLACK:
            if sensor == "L":
                self.LWhiteMap = 0
                self.LBlackMap += 1
                # self.LgreenMap = 0
            elif sensor == "R":
                self.RWhiteMap = 0
                self.RBlackMap += 1
                # self.RgreenMap = 0
                
        elif throwler == Color.GREEN:
            if sensor == "L":
                self.LWhiteMap = 0
                self.LBlackMap = 0
                self.LgreenMap += 1
            elif sensor == "R":
                self.RWhiteMap = 0
                self.RBlackMap = 0
                self.RgreenMap += 1


if __name__ == "__main__":
    robotBrain = LineFollower()
    robotBrain.run()