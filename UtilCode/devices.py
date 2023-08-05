from parameters import Parametros

class Devices:
    brain = EV3Brick() # Cerebro
        
    RColorSensor = ColorSensor(Port.S2) # Sensor de cor direito
    LColorSensor = ColorSensor(Port.S1) # Sensor de cor esquerdo
    FColorSensor = ColorSensor(Port.S4) # Sensor de cor frontal

    LMotor = Motor(Port.B) # Motor esquerdo
    RMotor = Motor(Port.A) # Motor direito

    motor = DriveBase(left_motor=Devices.LMotor, right_motor=Devices.RMotor, wheel_diameter=Parametros.wheel_diameter, axle_track=Parametros.axle_track)
    
    ultraSonic =  UltrasonicSensor(Port.S3) # Sensor ultrassonico
    
    grab = Motor(Port.C) # Motor de agarrar
    cage = Motor(Port.D) # Motor da jaula
    