# 
#  !!! CODIGO NÃO EXECUTAVEL !!!
#  !!! APENAS PARA TESTES !!!
# 
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
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
        color = sensor.color()
        
        return color
        
    # def check(sensor):
    #     if not ColorCheck.mapeamento:
    #         ColorCheck.mapeamento = getJSON()
            
    #     RGB = sensor.rgb()
    #     red = int(RGB[0])
    #     green = int(RGB[1])
    #     blue = int(RGB[2])
    #     color = sensor.color()
        
    #     if (ColorCheck.checkProximo([red, green, blue], [ColorCheck.mapeamento[0][0], ColorCheck.mapeamento[0][1], ColorCheck.mapeamento[0][2]]) or color == Color.WHITE):
    #         return Color.WHITE
        
    #     elif (ColorCheck.checkProximo([red, green, blue], [ColorCheck.mapeamento[1][0], ColorCheck.mapeamento[1][1], ColorCheck.mapeamento[1][2]]) or (red + green + blue) < 15):
    #         return Color.BLACK
        
    #     elif (ColorCheck.checkProximo([red, green, blue], [ColorCheck.mapeamento[2][0], ColorCheck.mapeamento[2][1], ColorCheck.mapeamento[2][2]]) or color == Color.GREEN):
    #         return Color.GREEN
        
    #     else:
    #         return None
        
    def checkProximo(data, data2):
        return ColorCheck.proximo(data[0], data2[0]) and ColorCheck.proximo(data[1], data2[1]) and ColorCheck.proximo(data[2], data[2])
    
    def proximo(value, value2):
        response = False
        
        if value2 <= value * 1.4 and value2 >= value * 0.6:
            response = True
            
        elif value < 8:
            if value2 >= (value - 3) and value2 <= (value + 3):
                response = True
        
        return response
        