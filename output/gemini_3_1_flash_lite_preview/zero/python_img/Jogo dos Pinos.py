import sys

def solve():
    tabuleiro = [list(line.strip()) for line in sys.stdin.readlines()]
    movimentos = 0
    
    # Direções: (dr, dc)
    direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for r in range(7):
        for c in range(7):
            # O pivô deve ser um pino
            if tabuleiro[r][c] == 'o':
                for dr, dc in direcoes:
                    r_alvo, c_alvo = r + dr, c + dc
                    r_dest, c_dest = r + 2 * dr, c + 2 * dc
                    
                    # Verifica se as coordenadas estão dentro do tabuleiro
                    if 0 <= r_dest < 7 and 0 <= c_dest < 7:
                        # Verifica se o alvo é um pino e o destino é um furo
                        if tabuleiro[r_alvo][c_alvo] == 'o' and tabuleiro[r_dest][c_dest] == '.':
                            movimentos += 1
                            
    print(movimentos)

if __name__ == '__main__':
    solve()