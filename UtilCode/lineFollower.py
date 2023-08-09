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
from pybricks.tools import wait
from pybricks.robotics import DriveBase

from UtilCode.colorCheck import ColorCheck
from UtilCode.greenState import GreenState
from UtilCode.arenaState import Arena
from UtilCode.devices import Devices
from UtilCode.parameters import Parametros


class LineFollower:
    def __init__(self):
        # Devices.brain.speaker.beep()
        # self.brain.screen.clear()
        # self.brain.light.on(Color.ORANGE)
        # self.brain.screen.draw_text(50, 60, "! FireWall !")

        self.RgreenMap = 0
        self.LgreenMap = 0

        self.RWhiteMap = 0
        self.LWhiteMap = 0

        self.RBlackMap = 0
        self.LBlackMap = 0

        self.RGpassed = False
        self.LGpassed = False

        self.Tl = False
        self.Tr = False

        self.greenState = GreenState()

    def run(self):
        while True:
            if Devices.ultraSonic.distance() < 50:
                self.passObstacle()

            if Devices.brain.buttons.pressed():
                Arena()

            self.checkLineNew()

    def checkLineNew(self):
        R = ColorCheck.check(Devices.RColorSensor)
        L = ColorCheck.check(Devices.LColorSensor)

        rm = 0
        lm = 0

        self.setState(R, "R")
        self.setState(L, "L")

        Devices.brain.screen.clear()
        Devices.brain.screen.print(self.RgreenMap)
        Devices.brain.screen.print(self.LgreenMap)

        # Controlador de linha direita
        if R == Color.WHITE:
            if self.RgreenMap >= 3 and self.LgreenMap >= 3:
                Devices.motor.stop()
                Devices.brain.speaker.beep()
                self.greenState.run(self.RgreenMap, self.LgreenMap)

            self.RgreenMap = 0
            self.LgreenMap = 0

            self.Tr = False

        elif R == Color.BLACK:
            if self.RgreenMap >= 3:
                Devices.motor.stop()
                Devices.brain.speaker.beep()
                self.greenState.run(self.RgreenMap, self.LgreenMap)
            else:
                self.Tr = True

            if self.RBlackMap >= 3:
                self.RgreenMap = 0

            if self.Tl:
                rm = 90
            else:
                rm = 80

        # Controlador de linha esquerda
        if L == Color.WHITE:
            if self.RgreenMap >= 3 and self.LgreenMap >= 3:
                Devices.motor.stop()
                Devices.brain.speaker.beep()
                self.greenState.run(self.RgreenMap, self.LgreenMap)

            self.RgreenMap = 0
            self.LgreenMap = 0

            self.Tl = False

        elif L == Color.BLACK:
            if self.LgreenMap >= 3:
                Devices.motor.stop()
                Devices.brain.speaker.beep()
                self.greenState.run(self.RgreenMap, self.LgreenMap)

            if self.LBlackMap >= 3:
                self.LgreenMap = 0
            if self.Tr:
                lm = 90
            else:
                lm = 80
                self.Tl = True

        Devices.motor.drive(Parametros.normalSpeed, lm - rm)

    def passObstacle(self):
        Devices.motor.stop()

        while Devices.ultraSonic.distance() > 100:
            if distance < 100:
                Devices.motor.straight((100 - distance) * -1)

        Devices.motor.turn(90)
        Devices.motor.straight(20 * 10)

        Devices.motor.turn(-90)
        Devices.motor.straight(40 * 10)

        Devices.motor.turn(-90)
        Devices.motor.straight(5 * 10)
        LBlack = False

        while True:
            Devices.motor.drive(Parametros.normalSpeed, 0)
            LS = ColorCheck.check(Devices.LColorSensor)
            RS = ColorCheck.check(Devices.RColorSensor)

            if LBlack and LS == Color.WHITE:
                break

            elif LS == Color.BLACK:
                Devices.motor.drive(Parametros.maxSpeed, 100)
                LBlack = True

            elif RS == Color.BLACK:
                Devices.motor.stop()
                Devices.motor.turn(-50)
                Devices.motor.straight(-3 * 10)
                Devices.motor.drive(Parametros.maxSpeed, -100)

                break
            else:
                Devices.motor.drive(Parametros.normalSpeed, 0)

    #
    # Esse metodo serve para detectar quantas vezes uma cor foi vista em sequencia
    # Objetivo: corrigir a margem de erro do sensor de cor
    #
    def setState(self, throwler, sensor):
        if throwler == Color.WHITE:
            if sensor == "L":
                self.LWhiteMap += 1
                self.LBlackMap = 0
                # self.LgreenMap = 0
            elif sensor == "R":
                self.RWhiteMap += 1
                self.RBlackMap = 0
                # self.RgreenMap = 0

        elif throwler == Color.BLACK:
            if sensor == "L":
                self.LWhiteMap = 0
                self.LBlackMap += 1
                # self.LgreenMap = 0
            elif sensor == "R":
                self.RWhiteMap = 0
                self.RBlackMap += 1
                # self.RgreenMap = 0

        elif throwler == Color.GREEN:
            if sensor == "L":
                self.LWhiteMap = 0
                self.LBlackMap = 0
                self.LgreenMap += 1
            elif sensor == "R":
                self.RWhiteMap = 0
                self.RBlackMap = 0
                self.RgreenMap += 1


if __name__ == "__main__":
    robotBrain = LineFollower()
    robotBrain.run()
