import sys

def solve():
    # Ler toda a entrada de uma vez
    input_data = sys.stdin.read().split()
    
    # O tabuleiro é fixo 15x15
    # Converter a entrada para uma lista de inteiros
    # São 15*15 = 225 inteiros
    if not input_data:
        return

    board = []
    try:
        iterator = iter(input_data)
        for _ in range(15):
            row = []
            for _ in range(15):
                row.append(int(next(iterator)))
            board.append(row)
    except StopIteration:
        pass # Caso de entrada incompleta, embora o problema garanta 15 linhas

    # Direções: (dr, dc)
    # Horizontal: (0, 1)
    # Vertical: (1, 0)
    # Diagonal Principal: (1, 1)
    # Diagonal Secundária: (1, -1)
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for r in range(15):
        for c in range(15):
            player = board[r][c]
            if player == 0:
                continue
            
            for dr, dc in directions:
                count = 0
                # Verificar 5 posições consecutivas
                for k in range(5):
                    nr, nc = r + dr * k, c + dc * k
                    
                    # Verificar limites
                    if 0 <= nr < 15 and 0 <= nc < 15:
                        if board[nr][nc] == player:
                            count += 1
                        else:
                            break # Sequência quebrada
                    else:
                        break # Fora do tabuleiro
                
                if count == 5:
                    # Verificar se a sequência é exatamente 5 (não 6 ou mais)
                    # Para isso, verificamos a pedra anterior e a posterior
                    # Pedra anterior (trás)
                    prev_r, prev_c = r - dr, c - dc
                    if 0 <= prev_r < 15 and 0 <= prev_c < 15:
                        if board[prev_r][prev_c] == player:
                            continue # É uma sequência de 6 ou mais, ignorar
                    
                    # Pedra posterior (frente)
                    next_r, next_c = r + dr * 5, c + dc * 5
                    if 0 <= next_r < 15 and 0 <= next_c < 15:
                        if board[next_r][next_c] == player:
                            continue # É uma sequência de 6 ou mais, ignorar
                    
                    # Se passou pelas verificações, é uma sequência válida de 5
                    print(player)
                    return

    print(0)

if __name__ == "__main__":
    solve()