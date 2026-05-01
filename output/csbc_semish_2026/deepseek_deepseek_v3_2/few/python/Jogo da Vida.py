import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    Q = int(next(it))
    
    grid = [list(next(it)) for _ in range(N)]
    
    for _ in range(Q):
        new_grid = [['0'] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                live_neighbors = 0
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == '1':
                            live_neighbors += 1
                if grid[i][j] == '1':
                    if live_neighbors == 2 or live_neighbors == 3:
                        new_grid[i][j] = '1'
                else:
                    if live_neighbors == 3:
                        new_grid[i][j] = '1'
        grid = new_grid
    
    sys.stdout.write('\n'.join(''.join(row) for row in grid))

if __name__ == "__main__":
    main()