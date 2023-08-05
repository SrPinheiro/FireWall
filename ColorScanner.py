#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Button, Color
from pybricks.tools import wait

ev3 = EV3Brick()
ev3.screen.clear()

Color = ColorSensor(Port.S2)

def saveJSON(json):
    texto = ""
    
    for i in range(3):
        texto += str(json[i][0]) + "\n"
        texto += str(json[i][1]) + "\n"
        texto += str(json[i][2]) + "\n"
        texto += ' \n'
    
    with open('colors', "w") as file:
        file.write(texto)

def searchColor(text):
    cor = Color.rgb()
    
    while True:
        ev3.screen.clear()
        cor = Color.rgb()
        
        ev3.screen.print(text)
        ev3.screen.print(cor)        
        
        wait(100)
        
        if ev3.buttons.pressed():
            break
    
    ev3.screen.clear()
    ev3.speaker.beep()
    ev3.screen.print("COR ATUALIZADA!")
    ev3.screen.print(cor)
    wait(2000)
    return(cor)
    
    
def run():
    ev3.speaker.beep()
    branco = searchColor("Cor BRANCA")
    preto = searchColor("Cor PRETA")
    verde = searchColor("Cor VERDE")
    
    
    ev3.screen.clear()
    ev3.screen.print("Deseja salvar ?")
    wait(5000)
    
    if not ev3.buttons.pressed():
        ev3.screen.clear()
        ev3.screen.print("Cancelando...!")
        wait(2000)
        run()
        
    else:
        json_data = [branco, preto, verde]
        saveJSON(json_data)

        ev3.screen.clear()
        ev3.speaker.beep()
        ev3.screen.print("Salvo com sucesso!")
        wait(2000)

if __name__ == "__main__":
    run()
    