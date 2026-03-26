import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    Q = int(data[idx]); idx += 1
    
    grid = []
    for i in range(N):
        row = list(map(int, list(data[idx]))); idx += 1
        grid.append(row)
    
    for _ in range(Q):
        new_grid = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                neighbors = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < N:
                            neighbors += grid[ni][nj]
                if grid[i][j] == 0:
                    if neighbors == 3:
                        new_grid[i][j] = 1
                    else:
                        new_grid[i][j] = 0
                else:
                    if neighbors == 2 or neighbors == 3:
                        new_grid[i][j] = 1
                    else:
                        new_grid[i][j] = 0
        grid = new_grid
    
    out = []
    for i in range(N):
        out.append(''.join(map(str, grid[i])))
    print('\n'.join(out))

solve()