#!/usr/bin/env pybricks-micropython

from UtilCode.devices import Devices
from UtilCode.colorCheck import ColorCheck
from pybricks.parameters import Port, Stop, Direction, Button, Color

corVerde = 0
corPreta = 0

while True:
    cor = ColorCheck.check(Devices.RColorSensor)
    cor2 = Devices.RColorSensor.color()
    
    Devices.brain.screen.clear()
    Devices.brain.screen.print(cor)
    Devices.brain.screen.print(cor2)
    Devices.brain.screen.print(corVerde)
    Devices.brain.screen.print(corPreta)
    
    if cor2 == Color.GREEN:
        corVerde += 1
        
        if corVerde >= 5:
            corPreta = 0
            
    if cor2 == Color.BLACK:
        corPreta += 1
        if corPreta >= 5:
            corVerde = 0