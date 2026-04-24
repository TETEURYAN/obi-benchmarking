import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    I = int(next(it)) - 1
    J = int(next(it)) - 1
    grid = []
    for _ in range(N):
        row = [int(next(it)) for _ in range(N)]
        grid.append(row)
    
    visited = [[False] * N for _ in range(N)]
    count = 0

    def dfs(i, j):
        nonlocal count
        visited[i][j] = True
        count += 1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # leste, sul, oeste, norte
        for dx, dy in dirs:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj] and grid[ni][nj] >= grid[i][j]:
                    dfs(ni, nj)
    
    dfs(I, J)
    print(count)

if __name__ == "__main__":
    main()