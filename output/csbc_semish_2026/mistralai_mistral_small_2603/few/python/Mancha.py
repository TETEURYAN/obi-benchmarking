
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    grid = data[1:n+1]

    # Encontrar todos os pixels da mancha
    pixels = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*':
                pixels.append((i, j))

    if len(pixels) < 2:
        print("S")
        return

    # Encontrar o pixel mais acima e mais à esquerda (canto superior esquerdo)
    start = min(pixels, key=lambda x: (x[0], x[1]))

    # BFS para calcular distâncias de Manhattan e distâncias reais
    manhattan_dist = {}
    real_dist = {}
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True
    real_dist[(start[0], start[1])] = 0
    manhattan_dist[(start[0], start[1])] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        i, j, dist = q.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == '*' and not visited[ni][nj]:
                visited[ni][nj] = True
                real_dist[(ni, nj)] = dist + 1
                manhattan_dist[(ni, nj)] = abs(ni - start[0]) + abs(nj - start[1])
                q.append((ni, nj, dist + 1))

    # Verificar se todas as distâncias reais são iguais às de Manhattan
    for pixel in pixels:
        if real_dist[pixel] != manhattan_dist[pixel]:
            print("N")
            return

    print("S")

if __name__ == "__main__":
    main()
