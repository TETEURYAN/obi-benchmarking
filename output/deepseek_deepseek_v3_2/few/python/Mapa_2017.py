import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    L = int(data[0])
    C = int(data[1])
    grid = []
    idx = 2
    for i in range(L):
        grid.append(data[idx])
        idx += 1
    
    # Encontrar posição inicial 'o'
    start = None
    for i in range(L):
        for j in range(C):
            if grid[i][j] == 'o':
                start = (i, j)
                break
        if start:
            break
    
    # DFS/BFS para seguir o caminho único
    current = start
    visited = set()
    visited.add(current)
    
    # Apenas um vizinho H no início
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while True:
        neighbors = []
        for dr, dc in dirs:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < L and 0 <= nc < C and grid[nr][nc] == 'H' and (nr, nc) not in visited:
                neighbors.append((nr, nc))
        
        # Se não há vizinhos H não visitados, chegamos ao fim
        if len(neighbors) == 0:
            break
        
        # Escolher o único vizinho válido
        next_pos = neighbors[0]
        visited.add(next_pos)
        current = next_pos
    
    # A posição atual é a última visitada
    print(current[0] + 1, current[1] + 1)

if __name__ == "__main__":
    solve()