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
        self.upGrab()
        
        while Devices.ultraSonic.distance() > 40:
            Devices.motor.drive(Parametros.maxSpeed, 0)    
        Devices.motor.stop()
            
        self.turnLeft()
        Devices.motor.straight(-100)
        
        self.downGrab()
        
        while True:
            while Devices.ultraSonic.distance() > 40:
                Devices.motor.drive(Parametros.maxSpeed, 0)

            Devices.motor.stop()
            Devices.motor.straight(-100)
            self.upGrab()
            self.verifyArena()
            self.turnLeft()
            Devices.motor.straight(100)
            self.turnLeft()
            
            self.downGrab()
                
                
    def verifyArena(self):
        Devices.motor.straight(100)
        if Devices.FColorSensor.color() == Color.BLACK:
            self.dispose()
        else:
            Devices.motor.straight(-50)
            
            

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
        Devices.grab.run(200)
        wait(500)
        
    def downGrab(self):
        Devices.grab.run(-200)
        wait(500)        
    def upCage(self):
        Devices.cage.run(200)
        wait(500)
        
    def downDownCage(self):
        Devices.cage.run(-200)
        wait(500)
        
        
    def dispose(self):
        self.upGrab()
        
        while Devices.ultraSonic.distance() > 50:
            Devices.motor.drive(Parametros.maxSpeed, 0)

        Devices.motor.stop()
        Devices.motor.straight(-10 * 10)
        
        self.turnBack()
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
            