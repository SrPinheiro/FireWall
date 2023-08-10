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

        self.RGreenMap = 0
        self.LGreenMap = 0

        self.RWhiteMap = 0
        self.LWhiteMap = 0

        self.RBlackMap = 0
        self.LBlackMap = 0

        self.RGpassed = False
        self.LGpassed = False
        
        self.ArenaMap = 0

        self.Tl = False
        self.Tr = False

        self.greenState = GreenState()

    def run(self):
        while True:
            if Devices.ultraSonic.distance() < 50:
                self.obstaculo()

            # if self.ArenaMap > 10:
            #     Arena()

            self.checkLineNew()

    def checkLineNew(self):
        R = ColorCheck.check(Devices.RColorSensor)
        L = ColorCheck.check(Devices.LColorSensor)

        rm = 0
        lm = 0

        self.setState(R, "R")
        self.setState(L, "L")
        
        corDec = False

        Devices.brain.screen.clear()
        Devices.brain.screen.print(self.RGreenMap)
        Devices.brain.screen.print(self.LGreenMap)

        # Controlador de linha direita
        # if R != Color.BLUE or L != Color.BLUE:
        #     self.ArenaMap = 0
        # else:
        #     self.ArenaMap += 1
            
        if R == Color.WHITE:
            if (
                self.RGreenMap >= Parametros.greenMap
                and self.LGreenMap >= Parametros.greenMap
            ):
                Devices.motor.stop()
                Devices.brain.speaker.beep()
                self.greenState.run(self.RGreenMap, self.LGreenMap)
            

            self.RGreenMap = 0
            self.LGreenMap = 0

            self.Tr = False

        elif R == Color.BLACK:
            corDec = True
            if self.RGreenMap >= Parametros.greenMap:
                Devices.motor.stop()
                Devices.brain.speaker.beep()
                self.greenState.run(self.RGreenMap, self.LGreenMap)
            else:
                self.Tr = True

            if self.RBlackMap >= 10:
                self.RGreenMap = 0
                
                if self.Tl:
                    rm = 80
                else:
                    rm = 70
                    self.Tr = True

        # Controlador de linha esquerda
        if L == Color.WHITE:
            if (
                self.RGreenMap >= Parametros.greenMap
                and self.LGreenMap >= Parametros.greenMap
            ):
                Devices.motor.stop()
                Devices.brain.speaker.beep()
                self.greenState.run(self.RGreenMap, self.LGreenMap)

            self.RGreenMap = 0
            self.LGreenMap = 0

            self.Tl = False

        elif L == Color.BLACK:
            corDec = True
            if self.LGreenMap >= Parametros.greenMap:
                Devices.motor.stop()
                Devices.brain.speaker.beep()
                self.greenState.run(self.RGreenMap, self.LGreenMap)

            if self.LBlackMap >= 10:
                self.LGreenMap = 0
                
                if self.Tr:
                    lm = 80
                else:
                    lm = 70
                    self.Tl = True
        speed = Parametros.normalSpeed
            
        Devices.motor.drive(speed, lm - rm)

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

    def obstaculo(self):
        Devices.motor.stop()
        LLine = False
        
        while Devices.ultraSonic.distance() < 190:
            Devices.motor.drive(-100, 0)

        Devices.motor.stop()
        Devices.motor.turn(60)

        Devices.motor.drive(100, -15)
        wait(7000)

        Bl = 0
        while True:
            if Bl > 3:
                LLine = True

            if Devices.LColorSensor.color() == Color.BLACK:
                Bl += 1

            elif Devices.LColorSensor.color() == Color.WHITE and LLine:
                Devices.motor.stop()
                Devices.motor.turn(50)
                break

            elif Devices.LColorSensor.color() == Color.WHITE:
                Bl = 0

    #
    # Esse metodo serve para detectar quantas vezes uma cor foi vista em sequencia
    # Objetivo: corrigir a margem de erro do sensor de cor
    #
    def setState(self, throwler, sensor):
        if throwler == Color.WHITE:
            if sensor == "L":
                self.LWhiteMap += 1
                self.LBlackMap = 0
                # self.LGreenMap = 0
            elif sensor == "R":
                self.RWhiteMap += 1
                self.RBlackMap = 0
                # self.RGreenMap = 0

        elif throwler == Color.BLACK:
            if sensor == "L":
                self.LWhiteMap = 0
                self.LBlackMap += 1
                # self.LGreenMap = 0
            elif sensor == "R":
                self.RWhiteMap = 0
                self.RBlackMap += 1
                # self.RGreenMap = 0

        elif throwler == Color.GREEN:
            if sensor == "L":
                self.LWhiteMap = 0
                self.LBlackMap = 0
                self.LGreenMap += 1
            elif sensor == "R":
                self.RWhiteMap = 0
                self.RBlackMap = 0
                self.RGreenMap += 1


if __name__ == "__main__":
    robotBrain = LineFollower()
    robotBrain.run()
