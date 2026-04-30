
def calcular_valor(carta, naipe_dominante):
    figura, naipe = carta[0], carta[1]
    valores = {'A': 1, 'J': 3, 'Q': 2, 'K': 4}
    if naipe == naipe_dominante:
        return valores[figura] * 2
    else:
        return valores[figura]

def main():
    cartas = [input().strip() for _ in range(7)]
    naipe_dominante = cartas[0][1]
    cartas_luana = cartas[1:4]
    cartas_edu = cartas[4:7]

    soma_luana = sum(calcular_valor(carta, naipe_dominante) for carta in cartas_luana)
    soma_edu = sum(calcular_valor(carta, naipe_dominante) for carta in cartas_edu)

    if soma_luana > soma_edu:
        print("Luana")
    elif soma_edu > soma_luana:
        print("Edu")
    else:
        print("empate")

if __name__ == "__main__":
    main()
