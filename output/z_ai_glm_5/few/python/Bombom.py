import sys

def main():
    # Leitura rápida de todas as entradas
    cartas = sys.stdin.read().split()
    
    if not cartas:
        return

    # O naipe dominante é o naipe da primeira carta
    # A carta é uma string de 2 caracteres, ex: "AC". O naipe é o índice 1.
    naipe_dominante = cartas[0][1]
    
    # Mapeamento das figuras para seus valores base
    valores_base = {
        'A': 10,
        'J': 11,
        'Q': 12,
        'K': 13
    }
    
    def calcular_pontos(indices):
        total = 0
        for i in indices:
            carta = cartas[i]
            figura = carta[0]
            naipe = carta[1]
            
            valor = valores_base[figura]
            if naipe == naipe_dominante:
                valor += 4
            
            total += valor
        return total
    
    # Luana possui as cartas de índice 1, 2 e 3
    pontos_luana = calcular_pontos([1, 2, 3])
    
    # Edu possui as cartas de índice 4, 5 e 6
    pontos_edu = calcular_pontos([4, 5, 6])
    
    if pontos_luana > pontos_edu:
        print("Luana")
    elif pontos_edu > pontos_luana:
        print("Edu")
    else:
        print("empate")

if __name__ == "__main__":
    main()