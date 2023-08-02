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
        
        self.maxSpeed = 90
        self.normalSpeed = 10
        self.turnAngle = 270
        self.blackReflection = 30
        
        self.lineReflection = 10
        self.whiteReflection = 40
        
        # self.brain.speaker.beep()
        self.brain.screen.clear()
        self.brain.screen.print("Line Follower instantiated")

    def run(self):
        # self.brain.speaker.beep()
        
        while True:
            sensorInformation = self.getLightInformation()
            leftCorrection = 0
            rightCorrection = 0
            
            if(sensorInformation["LColor"] == Color.GREEN or sensorInformation["RColor"] == Color.GREEN):
                self.GreenState()
            
            leftCorrection = sensorInformation["LReflection"] - self.lineReflection
            rightCorrection = sensorInformation["RReflection"] - self.lineReflection
                
            self.brain.screen.clear()
            self.brain.screen.print(leftCorrection)
            self.brain.screen.print(rightCorrection)
            
            if (sensorInformation["LReflection"] > self.blackReflection and sensorInformation["RReflection"] < self.blackReflection):                
                self.LMotor.run(self.normalSpeed + leftCorrection ** 1.3)
                
            elif (sensorInformation["RReflection"] > self.blackReflection and sensorInformation["LReflection"] < self.blackReflection):
                self.RMotor.run(self.normalSpeed + rightCorrection * 1.3)
                
            else:
                self.LMotor.run(int(leftCorrection ** 1.3))
                self.RMotor.run(int(rightCorrection ** 1.3))
                
                
            wait(10)
            
                        
    def GreenState(self):
        # self.brain.speaker.beep()
        self.brain.screen.clear()
        self.brain.screen.print("Green State")
        # self.drive(0)
        wait(2000)
        pass
    
    def passObstacle(self):
        self.brain.speaker.beep()
        self.brain.screen.clear()
        self.brain.screen.print("Pass Obstacle")
        wait(2000)
        pass
    
    def getLightInformation(self):
        
        LReflection = int(self.LColorSensor.reflection())
        RReflection = int(self.RColorSensor.reflection())
        
        LColor = self.LColorSensor.color()
        RColor = self.RColorSensor.color()
        
        return {
            "LReflection": LReflection,
            "RReflection": RReflection,
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