import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    grid = [list(next(it)) for _ in range(n)]
    
    # Encontra o primeiro pixel da mancha
    start = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*':
                start = (i, j)
                break
        if start:
            break
    
    # BFS para coletar todos os pixels da mancha
    mancha = []
    visited = [[False] * n for _ in range(n)]
    queue = [start]
    visited[start[0]][start[1]] = True
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    
    while queue:
        r, c = queue.pop()
        mancha.append((r, c))
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == '*' and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc))
    
    # Para cada pixel na mancha, calcula distância de Manhattan e BFS
    for i in range(len(mancha)):
        sr, sc = mancha[i]
        dist = [[-1] * n for _ in range(n)]
        dist[sr][sc] = 0
        queue = [(sr, sc)]
        idx = 0
        while idx < len(queue):
            r, c = queue[idx]
            idx += 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == '*' and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        
        # Verifica condição para todos os pixels da mancha
        for j in range(i+1, len(mancha)):
            tr, tc = mancha[j]
            if dist[tr][tc] != abs(sr - tr) + abs(sc - tc):
                print("N")
                return
    
    print("S")

if __name__ == "__main__":
    main()