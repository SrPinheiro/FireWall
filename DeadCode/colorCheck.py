from UtilCode.getColors import getJSON

class ColorCheck:
    mapeamento = {}
        
    def check(sensor):
        if not ColorCheck.mapeamento:
            ColorCheck.mapeamento = getJSON()
            
        RGB = sensor.rgb()
        red = int(RGB[0])
        green = int(RGB[1])
        blue = int(RGB[2])
        
        if (ColorCheck.checkProximo([red, green, blue], [ColorCheck.mapeamento[0][0], ColorCheck.mapeamento[0][1], ColorCheck.mapeamento[0][2]])):
            return Color.WHITE
        
        elif (ColorCheck.checkProximo([red, green, blue], [ColorCheck.mapeamento[1][0], ColorCheck.mapeamento[1][1], ColorCheck.mapeamento[1][2]])):
            return Color.BLACK
        
        elif (ColorCheck.checkProximo([red, green, blue], [ColorCheck.mapeamento[2][0], ColorCheck.mapeamento[2][1], ColorCheck.mapeamento[2][2]])):
            return Color.GREEN
        
        else:
            return "none"
        
    def checkProximo(data, data2):
        return ColorCheck.proximo(data[0], data2[0]) and ColorCheck.proximo(data[1], data2[1]) and ColorCheck.proximo(data[2], data[2])
    
    def proximo(value, value2):
        response = False
        
        if value2 <= value * 1.5 and value2 >= value * 0.5:
            response = True
            
        elif value < 8:
            if value2 > (value - 3) and value2 < (value + 3):
                response = True
        
        return response
    
    def checkLineOp(self):
        RColor = ColorCheck.checkR(Devices.RColorSensor)
        LColor = ColorCheck.checkL(Devices.LColorSensor)
        
        if (LColor == Color.GREEN or RColor == Color.GREEN):
            # Devices.motor.stop()
            # self.greenState.run()
            Devices.brain.speaker.beep()
        
        if (LColor == Color.BLACK or RColor == Color.BLACK):
            self.makeTurn()
            
        Devices.motor.drive(Devices.maxSpeed, 0)
        
    def makeTurn(self):        
        while True:
            R = ColorCheck.check(Devices.RColorSensor)
            L = ColorCheck.check(Devices.LColorSensor)
            
            if(R == Color.BLACK and L == Color.BLACK):
                Devices.motor.drive(Parametros.normalSpeed, 0)
                
            elif(R == Color.GREEN or L == Color.GREEN):
                # self.greenState()
                "a"
                
            elif(R == Color.WHITE and L == Color.WHITE):
                break
            
            elif(R == Color.BLACK and L == Color.WHITE):
                Devices.motor.drive(Parametros.normalSpeed, 95)
                
            elif (R == Color.WHITE and L == Color.BLACK):
                Devices.motor.drive(Parametros.normalSpeed, -95)
                
            wait(50)
        