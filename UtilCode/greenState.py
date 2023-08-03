from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class GreenState:
    def __init__(self):
        self.brain = EV3Brick()
        
        self.RColorSensor = ColorSensor(Port.S1)
        self.LColorSensor = ColorSensor(Port.S2)
        
        self.LMotor = Motor(Port.B)
        self.RMotor = Motor(Port.A)

        self.motor = DriveBase(left_motor=self.LMotor, right_motor=self.RMotor, wheel_diameter=55.5, axle_track=104)
        
        self.R = False
        self.L = False
        
        self.turnAngle = 30
        
        self.motor.drive(0,0)
    
    def run(self):
        self.startCheck()
        
        
    def startCheck(self):
        self.RTurn()
        wait(100)
        self.checkR()
        
        self.LTurn()
        self.LTurn()
        self.checkL()
        
        self.RTurn()
        
        if(self.R and self.L):
            self.turn360() #Dar a volta
        
        elif(self.R and not self.L):
            self.TurnLeft() #Ir a la esquerda
        
        elif(not self.R and self.L):
            self.TurnRight() #Ir a la direita
        else:
            self.walkStraight() #Andar em frente
        
    def turn360(self):
        pass
    
    def TurnLeft(self):
        pass
        
    def TurnRight(self):
        pass
    
    def walkStraight(self):
        pass
        
    
    def checkR(self):
        colorData = self.getLightInformation()
        if(colorData["RColor"] == Color.GREEN):
            R = True
            
    def checkL(self):
        colorData = self.getLightInformation()
        if(colorData["LColor"] == Color.GREEN):
            L = True
        
    
    def RTurn(self):
        self.motor.turn(self.turnAngle)
        
    def LTurn(self):
        self.motor.turn(self.turnAngle * -1)
    