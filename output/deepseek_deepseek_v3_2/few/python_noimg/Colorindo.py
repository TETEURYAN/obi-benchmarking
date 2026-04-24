import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    X = int(next(it))
    Y = int(next(it))
    K = int(next(it))
    
    # Ajuste para índices 0-based
    start_r = N - X
    start_c = Y - 1
    
    # Inicializa a grade: 0 = vazio, 1 = cheio
    grid = [[0] * M for _ in range(N)]
    
    # Marca os quadrados cheios
    for _ in range(K):
        A = int(next(it))
        B = int(next(it))
        r = N - A
        c = B - 1
        grid[r][c] = 1
    
    # BFS
    from collections import deque
    q = deque()
    q.append((start_r, start_c))
    grid[start_r][start_c] = 2  # Marca como visitado
    count = 1
    
    # 8 direções
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0),  (1, 1)]
    
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
                grid[nr][nc] = 2
                count += 1
                q.append((nr, nc))
    
    print(count)

if __name__ == "__main__":
    main()