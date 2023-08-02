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

        self.motor = DriveBase(left_motor=Motor(Port.B), right_motor=Motor(Port.A), wheel_diameter=55.5, axle_track=104)
        
        self.maxSpeed = 90
        self.normalSpeed = 70
        self.turnAngle = 270
        self.blackReflection = 40
        
        self.lineReflection = 5
        self.whiteReflection = 50
        
        self.brain.speaker.beep()
        self.brain.screen.clear()
        self.brain.screen.print("Line Follower instantiated")

    def run(self):
        self.brain.speaker.beep()
        
        while True:
            sensorInformation = self.getLightInformation()
            leftCorrection = 0
            rightCorretion = 0
            
            if(sensorInformation["LColor"] == Color.GREEN or sensorInformation["RColor"] == Color.GREEN):
                self.GreenState()
            
            elif( not (sensorInformation["LReflection"] < self.blackReflection and sensorInformation["RReflection"] < self.blackReflection)):
                leftCorrection = sensorInformation["LReflection"] - self.lineReflection
                rightCorretion = sensorInformation["RReflection"] - self.lineReflection
                
            correction = leftCorrection - rightCorretion           
            
            self.drive(correction)
            wait(10)
            
                        
    def GreenState(self):
        self.brain.speaker.beep()
        self.brain.screen.clear()
        self.brain.screen.print("Green State")
        self.drive(0)
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
    
    def drive(self, angle, speed=self.normalSpeed):
        self.drive(speed, angle)
    
if __name__ == "__main__":
    robotBrain = LineFollower()
    robotBrain.run()