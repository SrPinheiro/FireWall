class Devices:
    brain = EV3Brick()
        
    RColorSensor = ColorSensor(Port.S2)
    LColorSensor = ColorSensor(Port.S1)

    LMotor = Motor(Port.B)
    RMotor = Motor(Port.A)

    motor = DriveBase(left_motor=Device.LMotor, right_motor=Device.RMotor, wheel_diameter=Parametros.wheel_diameter, axle_track=Parametros.axle_track)
    
    ultraSonic =  UltrasonicSensor(Port.S3)
    
    cageMotor = Motor(Port.C)
    
class Parametros:
    maxSpeed = 70
    normalSpeed = 50
    minSpeed = 30
    
    wheel_diameter = 35 #Diametro da roda
    axle_track = 210 # Distancia entre as rodas