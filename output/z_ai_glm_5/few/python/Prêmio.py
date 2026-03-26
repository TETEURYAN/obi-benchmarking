import sys

def main():
    # Leitura rápida de todos os dados de entrada
    data = sys.stdin.read().split()
    
    if not data:
        return

    # Conversão dos valores de entrada para inteiros
    # P: pães, D: doces, B: bolos
    p = int(data[0])
    d = int(data[1])
    b = int(data[2])

    # Cálculo da pontuação total
    # Pão = 1 ponto, Doce = 2 pontos, Bolo = 3 pontos
    total = p + (d * 2) + (b * 3)

    # Determinação do prêmio baseado na pontuação
    if total >= 150:
        print('B')
    elif total >= 120:
        print('D')
    elif total >= 100:
        print('P')
    else:
        print('N')

if __name__ == "__main__":
    main()