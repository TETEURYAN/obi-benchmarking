import sys

def solve():
    grid = [list(line) for line in sys.stdin.read().splitlines() if line]
    if not grid:
        return
    
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # Direções: (dr, dc) para o movimento do pivô
    # O movimento é: Pivô -> Alvo -> Destino
    # Se o pivô está em (r, c), o alvo está em (r+dr, c+dc) e o destino em (r+2*dr, c+2*dc)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for r in range(rows):
        for c in range(cols):
            # O pivô deve ser um pino 'o'
            if grid[r][c] == 'o':
                for dr, dc in directions:
                    r_alvo, c_alvo = r + dr, c + dc
                    r_dest, c_dest = r + 2 * dr, c + 2 * dc
                    
                    # Verifica limites do tabuleiro
                    if 0 <= r_dest < rows and 0 <= c_dest < cols:
                        # Verifica se o alvo é um pino e o destino é um furo
                        if grid[r_alvo][c_alvo] == 'o' and grid[r_dest][c_dest] == '.':
                            count += 1
                            
    print(count)

if __name__ == '__main__':
    solve()