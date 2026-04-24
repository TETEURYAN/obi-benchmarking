import sys

def main():
    # Leitura rápida de todos os dados de entrada
    data = sys.stdin.read().split()
    
    if not data:
        return

    # Extraindo os valores conforme a ordem da entrada
    # A1: Ataque do jogador 1
    # D1: Defesa do jogador 1
    # A2: Ataque do jogador 2
    # D2: Defesa do jogador 2
    A1 = int(data[0])
    D1 = int(data[1])
    A2 = int(data[2])
    D2 = int(data[3])

    # Verificações de sobrevivência baseadas nas regras:
    # Um jogador sobrevive se sua defesa for IGUAL ao ataque do oponente.
    # Um jogador desmaia se sua defesa for DIFERENTE do ataque do oponente.
    
    p1_sobrevive = (D1 == A2)
    p2_sobrevive = (D2 == A1)

    # Determinação do resultado
    if p1_sobrevive and not p2_sobrevive:
        print(1)
    elif p2_sobrevive and not p1_sobrevive:
        print(2)
    else:
        # Casos de empate: ambos sobrevivem ou ambos desmaiam
        print(-1)

if __name__ == "__main__":
    main()