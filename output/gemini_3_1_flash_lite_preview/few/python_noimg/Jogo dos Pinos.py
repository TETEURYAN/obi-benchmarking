import sys

def solve():
    grid = [list(line.strip()) for line in sys.stdin.readlines() if line.strip()]
    
    rows = 7
    cols = 7
    moves = 0
    
    # Direções: (dr, dc)
    # Para um pino em (r, c) pular sobre (r+dr, c+dc) para (r+2*dr, c+2*dc)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for r in range(rows):
        for c in range(cols):
            # O pivô deve ser um pino
            if grid[r][c] == 'o':
                for dr, dc in directions:
                    r_alvo, c_alvo = r + dr, c + dc
                    r_dest, c_dest = r + 2 * dr, c + 2 * dc
                    
                    # Verifica limites do tabuleiro
                    if 0 <= r_dest < rows and 0 <= c_dest < cols:
                        # Verifica se o alvo é pino e o destino é furo
                        if grid[r_alvo][c_alvo] == 'o' and grid[r_dest][c_dest] == '.':
                            moves += 1
                            
    print(moves)

if __name__ == '__main__':
    solve()