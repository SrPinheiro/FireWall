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
        
        if (red >= 40 and green >= 40 and blue >= 70):
            return Color.WHITE
        
        elif (red <= 7 and green <= 8 and blue <= 8):
            return Color.BLACK
        
        elif ( green > (red + blue) or (green >= 9 and red < 10 and blue >= 10)):
            return Color.GREEN
        
        else:
            return "none"