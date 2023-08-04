def getJSON():
    conteudo_json = ""
    
    with open("../colors.JSON", "r") as arquivo_json:
        conteudo_json = arquivo_json.read()
    
    pilha = []
    objeto_atual = None
    chave_atual = None
    dentro_de_string = False
    string_atual = ''

    for char in conteudo_json:
        if char == '{':
            if objeto_atual is None:
                objeto_atual = {}
            else:
                pilha.append(objeto_atual)
                objeto_atual[chave_atual] = {}
                objeto_atual = objeto_atual[chave_atual]
            chave_atual = None
        elif char == '}':
            if pilha:
                objeto_atual = pilha.pop()
        elif char == '"':
            if dentro_de_string:
                dentro_de_string = False
                if chave_atual is None:
                    chave_atual = string_atual
                else:
                    objeto_atual[chave_atual] = string_atual
                    chave_atual = None
                string_atual = ''
            else:
                dentro_de_string = True
        elif dentro_de_string:
            string_atual += char

    return objeto_atual
