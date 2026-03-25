import sys
from collections import deque

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    grid = []
    start = None
    end = None
    for i in range(N):
        row = []
        for j in range(M):
            val = int(next(it))
            row.append(val)
            if val == 2:
                start = (i, j)
            elif val == 3:
                end = (i, j)
        grid.append(row)
    
    # BFS para encontrar o caminho mais curto de start até end
    # mas só podemos andar por salas com valor 1, 2 ou 3
    # (2 e 3 são especiais, mas também são parte do caminho)
    # O problema garante que existe um único caminho seguindo as estrelinhas (valor 1),
    # mas vamos usar BFS para garantir a menor distância.
    
    dist = [[-1] * M for _ in range(N)]
    q = deque()
    q.append(start)
    dist[start[0]][start[1]] = 0
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while q:
        x, y = q.popleft()
        if (x, y) == end:
            break
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] != 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    
    # A resposta é a distância da sala 2 até a sala 3
    print(dist[end[0]][end[1]])

if __name__ == "__main__":
    main()