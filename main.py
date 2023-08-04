#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from UtilCode.lineFollower import LineFollower
from pybricks.tools import wait

ev3 = EV3Brick()
robotBrain = LineFollower()
robotBrain.run()

    
