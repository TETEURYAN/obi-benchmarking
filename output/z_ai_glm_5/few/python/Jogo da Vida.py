import sys

# Aumentar o limite de recursão, embora não seja estritamente necessário para esta solução iterativa.
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        q = int(next(iterator))
    except StopIteration:
        return

    # Leitura da grade inicial
    grid = []
    for _ in range(n):
        row_str = next(iterator)
        # Converte a string de caracteres '0' e '1' para uma lista de inteiros
        grid.append([int(c) for c in row_str])

    # Definição das 8 direções vizinhas (horizontal, vertical e diagonal)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    # Simulação dos Q passos
    for _ in range(q):
        new_grid = [[0] * n for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                # Contagem de vizinhos vivos
                live_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Verifica se o vizinho está dentro dos limites da matriz
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            live_neighbors += 1
                
                # Aplicação das regras do Jogo da Vida
                if grid[r][c] == 1:
                    # Célula viva
                    if live_neighbors == 2 or live_neighbors == 3:
                        new_grid[r][c] = 1
                    else:
                        new_grid[r][c] = 0
                else:
                    # Célula morta
                    if live_neighbors == 3:
                        new_grid[r][c] = 1
                    else:
                        new_grid[r][c] = 0
        
        # Atualiza o estado do jogo para o próximo passo
        grid = new_grid

    # Preparação da saída
    output_lines = []
    for row in grid:
        # Converte a lista de inteiros de volta para string
        output_lines.append("".join(map(str, row)))
    
    # Imprime o resultado
    sys.stdout.write("\n".join(output_lines) + "\n")

if __name__ == "__main__":
    solve()