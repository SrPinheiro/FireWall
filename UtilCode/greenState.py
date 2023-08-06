from pybricks.tools import wait
from pybricks.parameters import Color

from UtilCode.devices import Devices
from UtilCode.parameters import Parametros

class GreenState:
    def __init__(self):   

        self.R = False
        self.L = False
        
        self.turnAngle = 30

    
    def run(self, r, l):
        Devices.motor.stop()
        
        if (r > 140):
            self.R = True
            
        if (l > 140):
            self.L = True
            
        if(self.R and self.L):
            self.turn180() #Dar a volta
            
        else:
            Devices.motor.straight(60)

            if(self.R and not self.L):
                self.TurnLeft() #Ir a la esquerda
            
            elif(not self.R and self.L):
                self.TurnRight() #Ir a la direita
                
            Devices.motor.straight(60) # andar em frente
            wait(1000)
        
    def turn180(self):
        Devices.motor.turn(180)
        
    def TurnLeft(self):
        Devices.motor.turn(-90)
        
    def TurnRight(self):
        Devices.motor.turn(90)
    
    def walkStraight(self):
        Devices.motor.straight(30)
            
    def checkR(self):
        colorData = Devices.RColorSensor.color()
        if(colorData == Color.GREEN):
            R = True
            
    def checkL(self):
        colorData = Devices.LColorSensor.color()
        if(colorData == Color.GREEN):
            L = True
        
    def RTurn(self):
        Devices.motor.turn(self.turnAngle)
        
    def LTurn(self):
        Devices.motor.turn(self.turnAngle * -1)
    