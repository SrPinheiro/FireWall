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

    def run(self):
        while True:
            RColor = ColorCheck.check(self.RColorSensor)
            LColor = ColorCheck.check(self.LColorSensor)
            
            distance = self.ultraSonic.distance()
            
            if (distance < 100):
                self.passObstacle()

            if (LColor == Color.GREEN or RColor == Color.GREEN):
                # self.motor.stop()
                # self.greenState()
                "a"
            
            if (LColor == Color.BLACK or RColor == Color.BLACK):
                self.makeTurn()
                
            self.motor.drive(self.maxSpeed, 0)

            wait(10)
            
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
                 
    def greenState(self):
        green = GreenState()
        green.run()
        
    
    def passObstacle(self):
        self.motor.stop()
        
        # while True:
        #     self.brain.speaker.beep()
            
        #     if Button.CENTER in self.brain.buttons.pressed():
        #         break
            
        #     wait(1000)
        
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