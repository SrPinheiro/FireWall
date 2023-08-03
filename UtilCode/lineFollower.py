from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class LineFollower:
    def __init__(self):
        self.brain = EV3Brick()
        
        self.RColorSensor = ColorSensor(Port.S1)
        self.LColorSensor = ColorSensor(Port.S2)
        
        self.LMotor = Motor(Port.B)
        self.RMotor = Motor(Port.A)

        self.motor = DriveBase(left_motor=self.LMotor, right_motor=self.RMotor, wheel_diameter=55.5, axle_track=104)
        
        self.maxSpeed = 120
        self.normalSpeed = 50
        self.blackReflection = 30
        
        self.lineReflection = 10
        self.whiteReflection = 40
        
        self.brain.screen.clear()
        self.brain.screen.print("Line Follower instantiated")

    def run(self):
        
        while True:
            sensorInformation = self.getLightInformation()
            
            
            if(sensorInformation["LColor"] == Color.GREEN or sensorInformation["RColor"] == Color.GREEN):
                self.motor.drive(0,0)
                self.greenState()
            
            if(sensorInformation["LColor"] == Color.BLACK or sensorInformation["RColor"] == Color.BLACK):
                self.makeTurn()
                
            self.motor.drive(self.maxSpeed, 0)

            wait(10)
            
    def makeTurn(self):        
        while True:
            R = self.RColorSensor.color()
            L = self.LColorSensor.color()
            
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
        self.motor.drive(0,0)
        L = False
        R = False
        
        colorData = self.getLightInformation()
        if(colorData["LColor"] == Color.GREEN):
            L = True

        if(colorData["RColor"] == Color.GREEN):
            R = True

        self.motor.turn(40)
        wait(1000)
        
        colorData = self.getLightInformation()
        if(colorData["LColor"] == Color.GREEN):
            L = True
            
        if(colorData["RColor"] == Color.GREEN):
            R = True
            
        self.motor.turn(-40)
        self.motor.turn(-40)
        wait(1000)
        colorData = self.getLightInformation()
        if(colorData["LColor"] == Color.GREEN):
            L = True

        if(colorData["RColor"] == Color.GREEN):
            R = True
            
        self.motor.turn(40)
        
        self.brain.screen.clear()
        if(L and R):
            self.brain.screen.print("IR RETOO")
        elif(L):
            self.brain.screen.print("IR ISQUERDA")
        elif(R):
            self.brain.screen.print("IR DIREITA")
        else:
            self.brain.screen.print("IR RETOO")
        
        wait(10000)
    
    def passObstacle(self):
        self.brain.speaker.beep()
        self.brain.screen.clear()
        self.brain.screen.print("Pass Obstacle")
        wait(2000)
        pass
    
    def getLightInformation(self):        
        LColor = self.LColorSensor.color()
        RColor = self.RColorSensor.color()
        
        return {
            "LColor": LColor,
            "RColor": RColor
        }

    def getTurnAngle(self, value):
        angle = self.turnAngle - value
        
        if (angle > 35):
            angle *= 0.5
            
        return angle
    
    def drive(self, angle, speed):
        self.motor.drive(speed, angle)
    
if __name__ == "__main__":
    robotBrain = LineFollower()
    robotBrain.run()