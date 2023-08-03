from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from greenState import GreenState
from colorCheck import ColorCheck

class LineFollower:
    def __init__(self):
        self.brain = EV3Brick()
        
        self.RColorSensor = ColorSensor(Port.S2)
        self.LColorSensor = ColorSensor(Port.S1)
        self.color =ColorCheck()

        self.LMotor = Motor(Port.B)
        self.RMotor = Motor(Port.A)

        self.motor = DriveBase(left_motor=self.LMotor, right_motor=self.RMotor, wheel_diameter=55.5, axle_track=104)
        
        self.ultraSonic =  UltrasonicSensor(Port.S3)
        
        self.maxSpeed = 120
        self.normalSpeed = 50
        self.blackReflection = 30
        
        self.lineReflection = 10
        self.whiteReflection = 40
        
        self.brain.screen.clear()
        self.brain.screen.print("Line Follower instantiated")

    def run(self):
        while True:
            RColor = self.color.check(self.RColorSensor)
            LColor = self.color.check(self.LColorSensor)
            
            distance = self.ultraSonic.distance()
            
            if (distance < 100):
                self.passObstacle()

            if (LColor == Color.GREEN or RColor == Color.GREEN):
                self.motor.drive(0,0)
                self.greenState()
            
            if (LColor == Color.BLACK or RColor == Color.BLACK):
                self.makeTurn()
                
            self.motor.drive(self.maxSpeed, 0)

            wait(10)
            
    def makeTurn(self):        
        while True:
            R = self.color.check(self.RColorSensor)
            L = self.color.check(self.LColorSensor)
            
            if(R == Color.BLACK and L == Color.BLACK):
                self.motor.drive(self.maxSpeed, 0)
                
            elif(R == Color.GREEN or L == Color.GREEN):
                self.greenState()
                break
                
            elif(R == Color.WHITE and L == Color.WHITE):
                break
            
            elif(R == Color.BLACK and L == Color.WHITE):
                self.motor.drive(self.normalSpeed, 150)
                
            elif (R == Color.WHITE and L == Color.BLACK):
                self.motor.drive(self.normalSpeed, -150)
                
            wait(50)
                 
    def greenState(self):
        green = GreenState()
        green.run()
        
    
    def passObstacle(self):
        self.motor.drive(0,0)
        self.brain.speaker.beep()
        wait(2000)
        
        self.motor.turn(90)
        self.motor.s
   
    def drive(self, angle, speed):
        self.motor.drive(speed, angle)
    
if __name__ == "__main__":
    robotBrain = LineFollower()
    robotBrain.run()