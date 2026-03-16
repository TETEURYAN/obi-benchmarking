import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    N = int(data[0])
    Q = int(data[1])
    grid = [list(map(int, list(data[2 + i].strip()))) for i in range(N)]

    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)]

    for _ in range(Q):
        new_grid = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                alive_neighbors = 0
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        alive_neighbors += grid[ni][nj]
                if grid[i][j] == 1:
                    if alive_neighbors == 2 or alive_neighbors == 3:
                        new_grid[i][j] = 1
                else:
                    if alive_neighbors == 3:
                        new_grid[i][j] = 1
        grid = new_grid

    out = [''.join(map(str, row)) for row in grid]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()
