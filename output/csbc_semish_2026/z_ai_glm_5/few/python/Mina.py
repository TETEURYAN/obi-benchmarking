import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
    except StopIteration:
        return

    grid = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(int(next(iterator)))
        grid.append(row)

    # 0-1 BFS
    # Distâncias inicializadas como infinito
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 0
    
    dq = deque()
    dq.append((0, 0))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while dq:
        r, c = dq.popleft()
        
        # Se chegamos ao destino, como usamos 0-1 BFS, esta é a distância mínima
        if r == n - 1 and c == n - 1:
            print(dist[r][c])
            return

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < n:
                cost = grid[nr][nc]
                new_dist = dist[r][c] + cost
                
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    if cost == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))
    
    print(dist[n-1][n-1])

if __name__ == "__main__":
    main()