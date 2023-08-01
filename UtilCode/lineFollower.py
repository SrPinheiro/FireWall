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
        
        self.motor = DriveBase(left_motor=Port.B, right_motor=Port.A, wheel_diameter=55.5, axle_track=104)
        
        self.maxSpeed = 150
        self.self.normalSpeed = 100
        self.minSpeed = 50
        self.turnAngle = 100
        
        self.brain.speaker.beep()
        self.brain.screen.clear()
        self.brain.screen.print("Line Follower instantiated")
        wait(2000)

    def run(self):
        self.brain.speaker.beep()
        self.brain.screen.clear()
        self.brain.screen.print("Line Follower")
        pass

    def GreenState(self):
        self.brain.speaker.beep()
        self.brain.screen.clear()
        self.brain.screen.print("Green State")
        pass
    
    def passObstacle(self):
        self.brain.speaker.beep()
        self.brain.screen.clear()
        self.brain.screen.print("Pass Obstacle")
        pass
    
    def getLightInformation(self):
        LReflection = int(self.LColorSensor.reflection())
        RReflection = int(self.RColorSensor.reflection())
        
        LColor = self.LColorSensor.Color()
        RColor = self.RColorSensor.Color()
        
        return {
            "LReflection": LReflection,
            "RReflection": RReflection,
            "LColor": LColor,
            "RColor": RColor
        }

if __name__ == "__main__":
    robotBrain = LineFollower()
    robotBrain.run()