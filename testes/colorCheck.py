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
    R, L = 0
    LastR, LastL = None
    
    def checkR(sensor):
        result = check(sensor)
        
        if result == Color.GREEN:
            ColorCheck.R += 1
            
            if ColorCheck.R >= 3:
                ColorCheck.LastR = result
                return result
            else:
                return ColorCheck.LastR
        else:
            ColorCheck.R = 0
            ColorCheck.LastR = result
            
    def checkL(sensor):
        result = check(sensor)
        
        if result == Color.GREEN:
            ColorCheck.L += 1
            
            if ColorCheck.L >= 3:
                ColorCheck.LastL = result
                return result
            else:
                return ColorCheck.LastL
        else:
            ColorCheck.L = 0
            ColorCheck.LastL = result
        
        
        return True

    
    def check(sensor):
        if not ColorCheck.mapeamento:
            ColorCheck.mapeamento = getJSON()
            
        RGB = sensor.rgb()
        red = int(RGB[0])
        green = int(RGB[1])
        blue = int(RGB[2])
        
        constant = sensor.color()
        
        if ((ColorCheck._checkProximo([red, green, blue], [ColorCheck.mapeamento[0][0], ColorCheck.mapeamento[0][1], ColorCheck.mapeamento[0][2]]) or (red > ColorCheck.mapeamento[0][0] and green > ColorCheck.mapeamento[0][1]) and blue > ColorCheck.mapeamento[0][2])) and constant == Color.WHITE:
            return Color.WHITE
        
        elif (ColorCheck._checkProximo([red, green, blue], [ColorCheck.mapeamento[1][0], ColorCheck.mapeamento[1][1], ColorCheck.mapeamento[1][2]]) and constant == Color.BLACK):
            return Color.BLACK
        
        elif (ColorCheck._checkProximo([red, green, blue], [ColorCheck.mapeamento[2][0], ColorCheck.mapeamento[2][1], ColorCheck.mapeamento[2][2]]) or constant == Color.GREEN ):
            return Color.GREEN
        
        else:
            return None
        
    def _checkProximo(data, data2):
        return ColorCheck._proximo(data[0], data2[0]) and ColorCheck._proximo(data[1], data2[1]) and ColorCheck._proximo(data[2], data[2])
    
    def _proximo(value, value2):
        response = False
        
        if value2 <= value * 1.3 and value2 >= value * 0.7:
            response = True
            
        elif value <= 8:
            if value2 > (value - 3) and value2 < (value + 3):
                response = True
        
        return response
        