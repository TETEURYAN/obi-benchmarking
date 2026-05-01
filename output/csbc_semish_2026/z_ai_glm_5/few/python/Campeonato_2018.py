import sys

def solve():
    # Leitura rápida da entrada
    input_data = sys.stdin.read().split()
    
    # Converte para inteiros
    players = list(map(int, input_data))
    
    # Encontra os índices (0 a 15) dos jogadores 1 e 9
    # Master Kung é o jogador 1, Master Lu é o jogador 9
    pos1 = players.index(1)
    pos9 = players.index(9)
    
    # Lógica para determinar a fase do confronto
    # Oitavas: jogadores estão no mesmo par (índices 0-1, 2-3, etc.)
    if pos1 // 2 == pos9 // 2:
        print("oitavas")
    # Quartas: jogadores estão no mesmo bloco de 4 (índices 0-3, 4-7, etc.)
    elif pos1 // 4 == pos9 // 4:
        print("quartas")
    # Semifinal: jogadores estão no mesmo bloco de 8 (índices 0-7, 8-15)
    elif pos1 // 8 == pos9 // 8:
        print("semifinal")
    # Final: jogadores estão em blocos de 8 diferentes
    else:
        print("final")

if __name__ == "__main__":
    solve()