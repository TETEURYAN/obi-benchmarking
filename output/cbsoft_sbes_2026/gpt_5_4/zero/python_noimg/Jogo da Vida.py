import sys

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    grid = [list(map(int, input().strip())) for _ in range(N)]

    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)]

    for _ in range(Q):
        nxt = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                alive = 0
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        alive += grid[ni][nj]
                if grid[i][j]:
                    if alive == 2 or alive == 3:
                        nxt[i][j] = 1
                else:
                    if alive == 3:
                        nxt[i][j] = 1
        grid = nxt

    sys.stdout.write('\n'.join(''.join(map(str, row)) for row in grid))

if __name__ == "__main__":
    main()
