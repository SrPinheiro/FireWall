#!/usr/bin/env pybricks-micropython

from UtilCode.devices import Devices
from UtilCode.colorCheck import ColorCheck

while True:
    cor = ColorCheck.check(Devices.RColorSensor)
    
    Devices.brain.screen.clear()
    Devices.brain.screen.print(cor)