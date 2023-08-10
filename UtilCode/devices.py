from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

from UtilCode.parameters import Parametros

# Classe responsavel por mapear todo o hardware do robo
class Devices:
    brain = EV3Brick() # Cerebro
        
    RColorSensor = ColorSensor(Port.S4) # Sensor de cor direito
    LColorSensor = ColorSensor(Port.S1) # Sensor de cor esquerdo
    FColorSensor = ColorSensor(Port.S2) # Sensor de cor fronta

    LMotor = Motor(Port.A) # Motor esquerdo
    RMotor = Motor(Port.D) # Motor direito

    motor = DriveBase(left_motor=LMotor, right_motor=RMotor, wheel_diameter=Parametros.wheel_diameter, axle_track=Parametros.axle_track)
    
    ultraSonic =  UltrasonicSensor(Port.S3) # Sensor ultrassonico
    
    grab = Motor(Port.B) # Motor de agarrar
    #cage = Motor(Port.C) # Motor da jaula
    