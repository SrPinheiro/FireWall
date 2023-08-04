def getJSON():
    objeto_final = []

    with open("../colors", "r") as file:
        for _ in range(3):
            conteudo_json = []
            for i in range(3):
                conteudo_json.append(int(file.readline()))

            file.readline()

            objeto_final.append(conteudo_json)

    return objeto_final


if __name__ == "__main__":
    print(getJSON())
