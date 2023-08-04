#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor,
from pybricks.parameters import Port, Button, Color
from pybricks.tools import wait

ev3 = EV3Brick()
ev3.screen.clear()

Color = ColorSensor(Port.S2)

def getJSON(json_str):
    stack = []
    obj = None
    key = None
    in_string = False
    current_string = ''

    for char in json_str:
        if char == '{':
            if obj is None:
                obj = {}
            else:
                stack.append(obj)
                obj[key] = {}
                obj = obj[key]
            key = None
        elif char == '}':
            if stack:
                obj = stack.pop()
        elif char == '"':
            if in_string:
                in_string = False
                if key is None:
                    key = current_string
                else:
                    obj[key] = current_string
                    key = None
                current_string = ''
            else:
                in_string = True
        elif in_string:
            current_string += char

    return obj

def saveJSON(json):
    JSONTEXT = f'''{{
    "CENTER": {{
        "BRANCO": {{
            "RED": "{json[0][0]}",
            "GREEN": "{json[0][1]}",
            "BLUE": "{json[0][2]}"
        }},
        "PRETO": {{
            "RED": "{json[1][0]}",
            "GREEN": "{json[1][1]}",
            "BLUE": "{json[1][2]}"
        }},
        "VERDE": {{
            "RED": "{json[2][0]}",
            "GREEN": "{json[2][1]}",
            "BLUE": "{json[2][2]}"
        }}
    }}
}}'''

    with open('colors.JSON', "w") as file:
        file.write(JSONTEXT)

def searchColor(text)
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
    ev3.screen.print("COR ATUALIZADA!")
    ev3.screen.print(Cor)
    wait(2000)
    return(cor)
    
    
def run():
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
        break
    
    json_data = [branco, preto, verde]
    saveJSON(json_data)

    ev3.screen.clear()
    ev3.screen.print("Salvo com sucesso!")
    wait(2000)

if __name__ == "__main__":
    run()
    