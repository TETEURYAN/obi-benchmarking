import sys
sys.setrecursionlimit(2000000)

def dfs(i, j):
    stack = [(i, j)]
    grid[i][j] = 0
    while stack:
        x, y = stack.pop()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                grid[nx][ny] = 0
                stack.append((nx, ny))

def main():
    global n, m, grid
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    grid = []
    for _ in range(n):
        row = [int(next(it)) for _ in range(m)]
        grid.append(row)
    
    manchas = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                manchas += 1
                dfs(i, j)
    print(manchas)

if __name__ == "__main__":
    main()