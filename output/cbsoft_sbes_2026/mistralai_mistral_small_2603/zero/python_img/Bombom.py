
def main():
    pontos = {
        'A': {'C': 10, 'E': 10, 'O': 10, 'P': 10},
        'J': {'C': 11, 'E': 11, 'O': 11, 'P': 11},
        'Q': {'C': 12, 'E': 12, 'O': 12, 'P': 12},
        'K': {'C': 13, 'E': 13, 'O': 13, 'P': 13}
    }
    dominante = None
    cartas = []
    for _ in range(7):
        carta = input().strip()
        cartas.append(carta)
        if _ == 0:
            dominante = carta[1]

    luana = cartas[1:4]
    edu = cartas[4:7]

    total_luana = 0
    for carta in luana:
        figura, naipe = carta[0], carta[1]
        if naipe == dominante:
            total_luana += pontos[figura]['C'] + 4
        else:
            total_luana += pontos[figura]['C']

    total_edu = 0
    for carta in edu:
        figura, naipe = carta[0], carta[1]
        if naipe == dominante:
            total_edu += pontos[figura]['C'] + 4
        else:
            total_edu += pontos[figura]['C']

    if total_luana > total_edu:
        print("Luana")
    elif total_edu > total_luana:
        print("Edu")
    else:
        print("empate")

if __name__ == "__main__":
    main()
