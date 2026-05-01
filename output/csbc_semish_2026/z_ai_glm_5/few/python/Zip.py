import sys

def calcular_pontuacao(c1, c2):
    soma = c1 + c2
    if c1 == c2:
        return 2 * soma
    if abs(c1 - c2) == 1:
        return 3 * soma
    return soma

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    cartas = list(map(int, input_data))
    
    lia1 = cartas[0]
    lia2 = cartas[1]
    carol1 = cartas[2]
    carol2 = cartas[3]
    
    pontuacao_lia = calcular_pontuacao(lia1, lia2)
    pontuacao_carol = calcular_pontuacao(carol1, carol2)
    
    if pontuacao_lia > pontuacao_carol:
        print("Lia")
    elif pontuacao_carol > pontuacao_lia:
        print("Carolina")
    else:
        print("empate")

if __name__ == "__main__":
    main()