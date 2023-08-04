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
        if (ColorCheck.mapeamento):
            ColorCheck.mapeamento = getJSON()["CENTER"]
            
        RGB = sensor.rgb()
        red = int(RGB[0])
        green = int(RGB[1])
        blue = int(RGB[2])
        
        if (red >= int(self.mapeamento["BRANCO"]["RED"])  and green >= int(self.mapeamento["BRANCO"]["GREEN"]) and blue >= int(self.mapeamento["BRANCO"]["BLUE"])):
            return Color.WHITE
        
        elif (red <= int(self.mapeamento["PRETO"]["RED"]) and green <= int(self.mapeamento["PRETO"]["GREEN"]) and blue <= int(self.mapeamento["PRETO"]["BLUE"])):
            return Color.BLACK
        
        elif (green > (int(self.mapeamento["VERDE"]["GREEN"]) + int(self.mapeamento["BRANCO"]["RED"])) or green + blue > red*2):
            return Color.GREEN
        
        else:
            return "none"