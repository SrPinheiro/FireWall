from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class ColorCheck:    
    def check(self, sensor):
        RGB = sensor.rgb()
        red = int(RGB[0])
        green = int(RGB[1])
        blue = int(RGB[2])
        
        if (red >= 70 and green >= 70 and blue >= 70):
            return Color.WHITE
        
        elif (red <= 15 and green <= 15 and blue <= 15):
            return Color.BLACK
        
        elif (green > 20 and green > (red + blue)):
            return Color.GREEN
        
        else:
            return "none"