import sys

cartas = [sys.stdin.readline().strip() for _ in range(7)]
naipe_dominante = cartas[0][1]

base = {'A': 1, 'J': 2, 'Q': 3, 'K': 4}

def valor(carta):
    figura, naipe = carta[0], carta[1]
    v = base[figura]
    if naipe == naipe_dominante:
        v += 4
    return v

luana = sum(valor(c) for c in cartas[1:4])
edu = sum(valor(c) for c in cartas[4:7])

if luana > edu:
    print("Luana")
elif edu > luana:
    print("Edu")
else:
    print("empate")