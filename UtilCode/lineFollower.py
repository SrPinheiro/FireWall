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
        self.normalSpeed = 50
        self.blackReflection = 30
        
        self.lineReflection = 10
        self.whiteReflection = 40

        self.brain.speaker.beep()
        self.brain.screen.clear()
        self.brain.light.on(Color.ORANGE)
        self.brain.screen.draw_text(50, 60, "! FireWall !")
        
        self.RgreenMap = 0
        self.LgreenMap = 0
        
        self.greenState = GreenState()

    def run(self):
        while True:
            self.checkLineOP()
            # self.checkLineNew()
            

            # wait(10)
            
    def checkLineOp(self):
        RColor = ColorCheck.checkR(self.RColorSensor)
        LColor = ColorCheck.checkL(self.LColorSensor)
        
        distance = self.ultraSonic.distance()
        
        if (distance < 100):
            self.passObstacle()

        if (LColor == Color.GREEN or RColor == Color.GREEN):
            # self.motor.stop()
            # self.greenState.run()
            ev3.speaker.beep()
        
        if (LColor == Color.BLACK or RColor == Color.BLACK):
            self.makeTurn()
            
        self.motor.drive(self.maxSpeed, 0)
                
    def checkLineNew(self):
        R = self.RColorSensor.color()
        L = self.LColorSensor.color()
        
        RM = 0
        LM = 0
        
        if R == Color.WHITE:
            RM = 0
        elif R == Color.BLACK:
            RM = 100
        elif R == Color.GREEN:
            self.RgreenMap += 1
            
            if (self.RgreenMap > 5):
                # self.greenState()
                ev3.speaker.beep()
                return
            
            else:
                self.motor.stop()
                return
            
        if L == Color.WHITE:
            LM = 0
        elif L == Color.BLACK:
            LM = 100
        elif L == Color.GREEN:
            self.LgreenMap += 1
            
            if (self.LgreenMap > 5):
                # self.greenState()
                ev3.speaker.beep()
                return
            else:
                self.motor.stop()
                return
            
        self.motor.drive(self.normalSpeed, RM - LM)
            
    def makeTurn(self):        
        while True:
            R = ColorCheck.check(self.RColorSensor)
            L = ColorCheck.check(self.LColorSensor)
            
            if(R == Color.BLACK and L == Color.BLACK):
                self.motor.drive(self.maxSpeed, 0)
                
            elif(R == Color.GREEN or L == Color.GREEN):
                # self.greenState()
                "a"
                
            elif(R == Color.WHITE and L == Color.WHITE):
                break
            
            elif(R == Color.BLACK and L == Color.WHITE):
                self.motor.drive(self.normalSpeed, 90)
                
            elif (R == Color.WHITE and L == Color.BLACK):
                self.motor.drive(self.normalSpeed, -90)
                
            wait(50)
    
    def passObstacle(self):
        self.motor.stop()
        
        distance = self.ultraSonic.distance()
        
        if (distance < 100):
            self.motor.straight((100 - distance) * -1)        
        
        self.motor.turn(90)
        self.motor.straight(100 * 10)
        
        self.motor.turn(-90)
        self.motor.straight(100 * 10)
        
        self.motor.turn(-90)
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
                self.motor.drive(self.maxSpeed, -100)
                break
            else:
                self.motor.drive(self.normalSpeed, 0)
                
    


if __name__ == "__main__":
    robotBrain = LineFollower()
    robotBrain.run()