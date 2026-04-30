
valores = {
    'A': {'C': 1, 'E': 2, 'O': 3, 'P': 4},
    'J': {'C': 5, 'E': 6, 'O': 7, 'P': 8},
    'Q': {'C': 9, 'E': 10, 'O': 11, 'P': 12},
    'K': {'C': 13, 'E': 14, 'O': 15, 'P': 16}
}

cartas = [input().strip() for _ in range(7)]
naipe_dom = cartas[0][1]

def valor(carta):
    fig = carta[0]
    naipe = carta[1]
    if naipe == naipe_dom:
        return valores[fig][naipe] + 16
    return valores[fig][naipe]

luana = sum(valor(c) for c in cartas[1:4])
edu = sum(valor(c) for c in cartas[4:7])

if luana > edu:
    print("Luana")
elif edu > luana:
    print("Edu")
else:
    print("empate")
