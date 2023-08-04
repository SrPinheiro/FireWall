def parse_json(json_str):
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
            "RED": "{json['CENTER']['BRANCO']['RED']}",
            "GREEN": "{json['CENTER']['BRANCO']['GREEN']}",
            "BLUE": "{json['CENTER']['BRANCO']['BLUE']}"
        }},
        "PRETO": {{
            "RED": "{json['CENTER']['PRETO']['RED']}",
            "GREEN": "{json['CENTER']['PRETO']['GREEN']}",
            "BLUE": "{json['CENTER']['PRETO']['BLUE']}"
        }},
        "VERDE": {{
            "RED": "{json['CENTER']['VERDE']['RED']}",
            "GREEN": "{json['CENTER']['VERDE']['GREEN']}",
            "BLUE": "{json['CENTER']['VERDE']['BLUE']}"
        }},
        "PRATA": {{
            "RED": "{json['CENTER']['PRATA']['RED']}",
            "GREEN": "{json['CENTER']['PRATA']['GREEN']}",
            "BLUE": "{json['CENTER']['PRATA']['BLUE']}"
        }}
    }}
}}'''

    with open('colors.JSON', "w") as file:
        file.write(JSONTEXT)