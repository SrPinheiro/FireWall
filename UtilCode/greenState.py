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

        self.motor = DriveBase(left_motor=self.LMotor, right_motor=self.RMotor, wheel_diameter=35, axle_track=210)
        
        self.R = False
        self.L = False
        
        self.turnAngle = 30
        
        self.motor.drive(0,0)
    
    def run(self, r, l):
        if (r > 140):
            self.R = True
        if (l > 140):
            self.L = True
            
        if(self.R and self.L):
            self.turn180() #Dar a volta
        else:
            self.motor.straight(60)

            if(self.R and not self.L):
                self.TurnLeft() #Ir a la esquerda
            
            elif(not self.R and self.L):
                self.TurnRight() #Ir a la direita
            else:
                self.walkStraight() #Andar em frente
                
            self.motor.straight(60)
            wait(1000)
        
        
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
        else:
            self.straight(30)

            if(self.R and not self.L):
                self.TurnLeft() #Ir a la esquerda
            
            elif(not self.R and self.L):
                self.TurnRight() #Ir a la direita
            else:
                self.walkStraight() #Andar em frente
            
            wait(5000)
        
    def turn180(self):
        self.motor.turn(180)
        
    
    def TurnLeft(self):
        self.motor.turn(-90)
        
    def TurnRight(self):
        self.motor.turn(90)
    
    def walkStraight(self):
        self.motor.straight(30)
            
        
    
    def checkR(self):
        colorData = self.RColorSensor.color()
        if(colorData == Color.GREEN):
            R = True
            
    def checkL(self):
        colorData = self.LColorSensor.color()
        if(colorData == Color.GREEN):
            L = True
        
    
    def RTurn(self):
        self.motor.turn(self.turnAngle)
        
    def LTurn(self):
        self.motor.turn(self.turnAngle * -1)
    