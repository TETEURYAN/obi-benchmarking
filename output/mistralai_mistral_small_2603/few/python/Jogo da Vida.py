import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    q = int(data[1])
    grid = data[2:2+n]

    current = [list(row) for row in grid]

    for _ in range(q):
        next_grid = [['0'] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            if current[ni][nj] == '1':
                                count += 1
                if current[i][j] == '1':
                    if count == 2 or count == 3:
                        next_grid[i][j] = '1'
                else:
                    if count == 3:
                        next_grid[i][j] = '1'
        current = next_grid

    for row in current:
        print(''.join(row))

if __name__ == "__main__":
    main()