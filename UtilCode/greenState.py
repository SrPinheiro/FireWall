from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    UltrasonicSensor,
    GyroSensor,
)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from UtilCode.devices import Devices
from UtilCode.parameters import Parametros

class GreenState:
    def __init__(self):
        self.R = False
        self.L = False

        self.turnAngle = 30

    def run(self, r, l):
        try:
            Devices.motor.stop()

            if r >= Parametros.greenMap:
                self.R = True

            if l >= Parametros.greenMap:
                self.L = True

            if self.R and self.L:
                self.turn180()  # Dar a volta
            else:
                Devices.motor.straight(60)

                if self.R and not self.L:
                    self.TurnLeft()  # Ir a la esquerda

                elif not self.R and self.L:
                    self.TurnRight()  # Ir a la direita
                else:
                    self.walkStraight()  # Andar em frente

                self.motor.straight(40)
                wait(1000)
        finally:
            self.L, self.R = False, False

    def turn180(self):
        Devices.motor.turn(180)

    def TurnLeft(self):
        Devices.motor.turn(-90)

    def TurnRight(self):
        Devices.motor.turn(90)

    def walkStraight(self):
        Devices.motor.straight(30)
