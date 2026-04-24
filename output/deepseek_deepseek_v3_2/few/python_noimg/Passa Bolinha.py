import sys
sys.setrecursionlimit(1000000)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    I = int(next(it)) - 1
    J = int(next(it)) - 1
    grid = [[int(next(it)) for _ in range(N)] for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    def dfs(r, c):
        if visited[r][c]:
            return
        visited[r][c] = True
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] >= grid[r][c]:
                dfs(nr, nc)
    
    dfs(I, J)
    count = sum(sum(row) for row in visited)
    print(count)

if __name__ == "__main__":
    main()