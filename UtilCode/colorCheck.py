from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from getColors import getJSON

class ColorCheck:
    mapeamento = {}
        
    def check(sensor):
        if not ColorCheck.mapeamento:
            ColorCheck.mapeamento = getJSON()
            
        RGB = sensor.rgb()
        red = int(RGB[0])
        green = int(RGB[1])
        blue = int(RGB[2])
        
        if (red >= int(self.mapeamento[0][0])  and green >= int(self.mapeamento[0][1]) and blue >= int(self.mapeamento[0][2])):
            return Color.WHITE
        
        elif (red <= int(self.mapeamento[1][0]) and green <= int(self.mapeamento[1][1]) and blue <= int(self.mapeamento[1][2])):
            return Color.BLACK
        
        elif (green > (int(self.mapeamento[2][1]) + int(self.mapeamento[0][0])) or green + blue > red*2):
            return Color.GREEN
        
        else:
            return "none"