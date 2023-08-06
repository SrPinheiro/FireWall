from pybricks.parameters import Color
from pybricks.tools import wait
    
from UtilCode.colorCheck import ColorCheck
from UtilCode.greenState import GreenState
from UtilCode.devices import Devices
from UtilCode.parameters import Parametros
from UtilCode.arenaState import ArenaState

# Classe responsavel por controlar o robo
class LineFollower:
    def __init__(self):        
        Devices.brain.speaker.beep()
        Devices.brain.screen.clear()
        Devices.brain.light.on(Color.ORANGE)
        Devices.brain.screen.draw_text(50, 60, "! FireWall !")
        
        # Contagem das cores
        self.RgreenMap = 0
        self.LgreenMap = 0
        
        self.RWhiteMap = 0
        self.LWhiteMap = 0
        
        self.RBlackMap = 0
        self.LBlackMap = 0
        
        self.greenState = GreenState()
        
        # Controle de giro
        self.TurningL = False
        self.TurningR = False
        
    # Tudo começa aqui...
    def run(self):
        while True:
            distance = Devices.ultraSonic.distance()
            if (distance < 50):
                self.passObstacle()
                
            self.checkLineNew()
    
    # Metodo responsavel por verificar as cores e responder de acordo
    def checkLineNew(self):
        R = Devices.RcolorSensor.color()
        L = Devices.LColorSensor.color()
        
        rm = 0
        lm = 0
        
        self.setState(R, "R")
        self.setState(L, "L")
        
        #Controlador de linha direita
        if R == Color.WHITE:
            if self.RWhiteMap > 40:
                if self.RgreenMap > 140 and self.LgreenMap > 140:
                    Devices.motor.stop()
                    Devices.brain.speaker.beep()
                    self.greenState.run(self.RgreenMap, self.LgreenMap)
                    
                    wait(1000)
                else:
                    self.TurningR = False
                
                self.RgreenMap = 0
                self.LgreenMap = 0
                
                self.TurningR = False

                
        elif R == Color.BLACK:
            if self.RBlackMap > 40:
                if self.RgreenMap > 140:
                    Devices.motor.stop()
                    Devices.brain.speaker.beep()
                    
                    self.greenState.run(self.RgreenMap, self.LgreenMap)
                    self.TurningR = False
                    
                    wait(1000)
                else:
                    self.TurningR = True
                    
                self.RgreenMap = 0
                
                if self.TurningL:
                    rm = 70
                else:
                    rm = 90
                    self.TurningR = True
                    

        #Controlador de linha esquerda
        if L == Color.WHITE:
            if self.LWhiteMap > 40:
                if self.RgreenMap > 140 and self.LgreenMap > 140:
                    Devices.motor.stop()
                    Devices.brain.speaker.beep()
                    self.greenState.run(self.RgreenMap, self.LgreenMap)
                    
                    wait(1000)
                
                self.RgreenMap = 0
                self.LgreenMap = 0
                
                self.TurningL = False

                
        elif L == Color.BLACK:
            if self.LBlackMap > 40:
                if self.LgreenMap > 140:
                    Devices.motor.stop()
                    Devices.brain.speaker.beep()
                    
                    self.greenState.run(self.RgreenMap, self.LgreenMap)
                    self.TurningL = False
                    
                    wait(1000)
                    
                self.LgreenMap = 0
                
                if self.TurningR:
                    lm = 70
                else:
                    lm = 90
                
        Devices.motor.drive(Parametros.normalSpeed, lm - rm)
        
        
    # Metodo responsavel por desviar de obstaculos
    def passObstacle(self):
        Devices.motor.stop()
        
        distance = Devices.ultraSonic.distance()
        
        while distance > 100:

            if (distance < 100):
                Devices.motor.straight((100 - distance) * -1)  
            
            distance = Devices.ultraSonic.distance()    
        
        Devices.motor.turn(-90)
        Devices.motor.straight(20 * 10)
        
        Devices.motor.turn(90)
        Devices.motor.straight(40 * 10)
        
        Devices.motor.turn(90)
        Devices.motor.straight(5 * 10)
        LBlack = False
        
        while True:
            Devices.motor.drive(Parametros.normalSpeed, 0)
            LS = ColorCheck.check(Devices.LColorSensor)
            RS = ColorCheck.check(Devices.RColorSensor)
            
            if LS == Color.BLACK and not LBlack:
                Devices.motor.drive(Devices.maxSpeed, 100)
                LBlack = True
                
            if (LBlack and LS == Color.WHITE and RS == Color.WHITE):
                Devices.motor.stop()
                break
                
            elif RS == Color.BLACK and LS == Color.BLACK:
                Devices.motor.stop()
                Devices.motor.straight(10 * 10)
                Devices.motor.turn(-90)
                Devices.motor.straight(-3 * 10)
                Devices.motor.drive(Devices.maxSpeed, -100)
                
                break
                
            elif (RS == Color.BLACK):
                Devices.motor.stop()
                Devices.motor.turn(-50)
                Devices.motor.straight(-3 * 10)
                Devices.motor.drive(Devices.maxSpeed, -100)
                
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