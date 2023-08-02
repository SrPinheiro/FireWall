#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from UtilCode.lineFollower import LineFollower
from pybricks.tools import wait
    

ev3 = EV3Brick()

try:
    while True:
        robotBrain = LineFollower()
        robotBrain.run()
    
except Exception as e:
    ev3.screen.clear()
    ev3.screen.print(e)
    wait(10000)
