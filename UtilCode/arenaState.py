from pybricks.parameters import Color
from pybricks.tools import wait
from UtilCode.devices import Devices
from UtilCode.parameters import Parametros

# Classe responsavel por controlar o robo quando entrar na arena
class Arena:
    
    def __init__(self):
        self.position = 90
        self.largura = 0
        self.alturaR = 0
        self.alturaL = 0
        
        self.run() # inicia o codigo
    
    def run(self):
        while True:
            if Devices.ultraSonic.distance() < 3.5:
                self.turnLeft()
                wait(500)
            
            if Devices.FColorSensor.reflection() > 40:
                Devices.motor.straight(-10 * 10)
                self.downGrab()
                wait(200)
                Devices.motor.straight(20 * 10)
                
                self.upGrab()
                wait(200)
                
            if Devices.ultraSonic.distance() < 3.5 and Devices.FColorSensor.color() == Color.BLACK:
                self.dispose()
                
            
            wait(1000)
        
    
    def mapArena(self):
        while Devices.ultraSonic.distance() > 3.5:
            Devices.motor.drive(Parametros.maxSpeed, 0)
            
            
        self.turnRight()
        
        while Devices.ultraSonic.distance() > 3.5:
            Devices.motor.drive(Parametros.maxSpeed, 0)
            
        self.turnBack()
        Devices.motor.drive(Parametros.maxSpeed * -1, 0)
        
        self.alturaL = Devices.ultraSonic.distance()
        
            
    def upGrab(self):
        Devices.grab.run_until_stalled(200, 0)
        
    def downGrab(self):
        Devices.grab.run_until_stalled(-200, 0)
        
    def upCage(self):
        Devices.cage.run_until_stalled(200, 0)
        
    def downDownCage(self):
        Devices.cage.run_until_stalled(-200, 0)
        
        
    def dispose(self):
        self.upGrab()
        
        while Devices.ultraSonic.distance() < 2000:
            Devices.motor.drive(Parametros.maxSpeed, 0)
        
        Devices.motor.straight(-10 * 10)
        
        self.turnback()
        self.upCage()
        
        Devices.motor.straight(-30 * 10)
        
        
    def turnLeft(self):
        Devices.motor.turn(Parametros.L90)
        
        if(self.position == 90):
            self.position = 180
        elif(self.position == 180):
            self.position = 270
        elif(self.position == 270):
            self.position = 0
        elif(self.position == 0):
            self.position = 90
            
    def turnRight(self):
        Devices.motor.turn(Parametros.R90)
        
        if(self.position == 90):
            self.position = 0
        elif(self.position == 0):
            self.position = 270
        elif(self.position == 270):
            self.position = 180
        elif(self.position == 180):
            self.position = 90
            
    def turnBack(self):
        Devices.motor.turn(180)
        
        if self.position == 0:
            self.position = 180
        elif self.position == 180:
            self.position = 0
        elif self.position == 90:
            self.position = 270
        elif self.position == 270:
            self.position = 90