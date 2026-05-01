
import sys

def main():
    grid = [sys.stdin.readline().strip() for _ in range(7)]
    count = 0

    for i in range(7):
        for j in range(7):
            if grid[i][j] != 'o':
                continue
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                pi, pj = i + di, j + dj
                if not (0 <= pi < 7 and 0 <= pj < 7):
                    continue
                if grid[pi][pj] != 'o':
                    continue
                ti, tj = pi + di, pj + dj
                if not (0 <= ti < 7 and 0 <= tj < 7):
                    continue
                if grid[ti][tj] == '.':
                    count += 1
    print(count)

if __name__ == "__main__":
    main()
