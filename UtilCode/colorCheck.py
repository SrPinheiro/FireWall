from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from UtilCode.getColors import getJSON

class ColorCheck:
    mapeamento = {}
    
    ler = True
    
    minRed = 0
    maxRed = 0
    
    minGreen = 0
    maxGreen = 0
    
    minBlue = 0
    maxBlue = 0
        
    def check(sensor):
        if not ColorCheck.mapeamento:
            ColorCheck.mapeamento = getJSON()
            
        RGB = sensor.rgb()
        red = int(RGB[0])
        green = int(RGB[1])
        blue = int(RGB[2])
        color = sensor.color()
        
        if (ColorCheck.checkProximo([red, green, blue], [ColorCheck.mapeamento[0][0], ColorCheck.mapeamento[0][1], ColorCheck.mapeamento[0][2]]) or color == Color.WHITE):
            return Color.WHITE

        elif (ColorCheck.checkProximo([red, green, blue], [ColorCheck.mapeamento[1][0], ColorCheck.mapeamento[1][1], ColorCheck.mapeamento[1][2]]) or (red + green + blue) < 10):
            return Color.BLACK
        
        elif (ColorCheck.checkProximo([red, green, blue], [ColorCheck.mapeamento[2][0], ColorCheck.mapeamento[2][1], ColorCheck.mapeamento[2][2]]) or color == Color.GREEN or (green > red + blue) or ColorCheck.checkVerde(red, green, blue)):
            return Color.GREEN
        
        
        
        else:
            return None
        
    def checkProximo(data, data2):
        return ColorCheck.proximo(data[0], data2[0]) and ColorCheck.proximo(data[1], data2[1]) and ColorCheck.proximo(data[2], data[2])
    
    def proximo(value, value2):
        response = False
        
        if value2 <= value * 1.35 and value2 >= value * 0.75:
            response = True
            
        elif value < 8:
            if value2 >= (value - 3) and value2 <= (value + 3):
                response = True
        
        return response
    
    def checkVerde(red, green, blue):
        if ColorCheck.ler:
            with open("green", "r") as file:
                ColorCheck.minRed = int(file.readline())
                ColorCheck.maxRed = int(file.readline())
                file.readline()
                ColorCheck.minGreen = int(file.readline())
                ColorCheck.maxGreen = int(file.readline())
                file.readline()
                ColorCheck.minBlue = int(file.readline())
                ColorCheck.maxBlue = int(file.readline())
            
            ColorCheck.ler = False
        
        response = True
        
        if ColorCheck.minRed > red > ColorCheck.maxRed:
            response = False
            
        if ColorCheck.minGreen > green > ColorCheck.maxGreen:
            response = False

        if ColorCheck.minBlue > blue > ColorCheck.maxBlue:
            response = False
            
        return response
