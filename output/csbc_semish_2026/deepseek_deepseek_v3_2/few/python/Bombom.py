import sys

def valor_carta(figura, naipe, naipe_dominante):
    valores_base = {'A': 10, 'J': 11, 'Q': 12, 'K': 13}
    bonus = 4 if naipe == naipe_dominante else 0
    return valores_base[figura] + bonus

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    cartas = data[:7]
    naipe_dominante = cartas[0][1]
    
    luana_cartas = cartas[1:4]
    edu_cartas = cartas[4:7]
    
    soma_luana = 0
    soma_edu = 0
    
    for carta in luana_cartas:
        figura, naipe = carta[0], carta[1]
        soma_luana += valor_carta(figura, naipe, naipe_dominante)
    
    for carta in edu_cartas:
        figura, naipe = carta[0], carta[1]
        soma_edu += valor_carta(figura, naipe, naipe_dominante)
    
    if soma_luana > soma_edu:
        print("Luana")
    elif soma_edu > soma_luana:
        print("Edu")
    else:
        print("empate")

if __name__ == "__main__":
    main()