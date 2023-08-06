from pybricks.parameters import Color
from pybricks.tools import wait
from UtilCode.devices import Devices
from UtilCode.parameters import Parametros

# Classe responsavel por controlar o robo quando entrar na arena
class Arena:
    position = 90
    largura = 0
    alturaR = 0
    alturaL = 0
    
    def run():
        while True:
            if Devices.ultraSonic.distance() < 3.5:
                Arena.turnLeft()
                wait(500)
            
            if Devices.FColorSensor.reflection() > 40:
                Devices.motor.straight(-10 * 10)
                Arena.downGrab()
                wait(200)
                Devices.motor.straight(20 * 10)
                
                Arena.upGrab()
                wait(200)
                
            if Devices.ultraSonic.distance() < 3.5 and Devices.FColorSensor.color() == Color.BLACK:
                Arena.dispose()
                
            
            wait(1000)
        
    
    def mapArena():
        while Devices.ultraSonic.distance() > 3.5:
            Devices.motor.drive(Parametros.maxSpeed, 0)
            
            
        Arena.turnRight()
        
        while Devices.ultraSonic.distance() > 3.5:
            Devices.motor.drive(Parametros.maxSpeed, 0)
            
        Arena.turnBack()
        Devices.motor.drive(Parametros.maxSpeed * -1, 0)
        
        Arena.alturaL = Devices.ultraSonic.distance()
        
            
    def upGrab():
        Devices.grab.run_until_stalled(200, 0)
        
    def downGrab():
        Devices.grab.run_until_stalled(-200, 0)
        
    def upCage():
        Devices.cage.run_until_stalled(200, 0)
        
    def downDownCage():
        Devices.cage.run_until_stalled(-200, 0)
        
        
    def dispose():
        Arena.upGrab()
        
        while Devices.ultraSonic.distance() < 2000:
            Devices.motor.drive(Parametros.maxSpeed, 0)
        
        Devices.motor.straight(-10 * 10)
        
        Arena.turnback()
        Arena.upCage()
        
        Devices.motor.straight(-30 * 10)
        
        
    def turnLeft():
        Devices.motor.turn(Parametros.L90)
        
        if(Arena.position == 90):
            Arena.position = 180
        elif(Arena.position == 180):
            Arena.position = 270
        elif(Arena.position == 270):
            Arena.position = 0
        elif(Arena.position == 0):
            Arena.position = 90
            
    def turnRight():
        Devices.motor.turn(Parametros.R90)
        
        if(Arena.position == 90):
            Arena.position = 0
        elif(Arena.position == 0):
            Arena.position = 270
        elif(Arena.position == 270):
            Arena.position = 180
        elif(Arena.position == 180):
            Arena.position = 90
            
    def turnBack():
        Devices.motor.turn(180)
        
        if Arena.position == 0:
            Arena.position = 180
        elif Arena.position == 180:
            Arena.position = 0
        elif Arena.position == 90:
            Arena.position = 270
        elif Arena.position == 270:
            Arena.position = 90