import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    vals = data[2:]

    grid = [vals[i*m:(i+1)*m] for i in range(n)]

    sr = sc = -1
    for i in range(n):
        row = grid[i]
        for j in range(m):
            if row[j] == 2:
                sr, sc = i, j
                break
        if sr != -1:
            break

    prev = (-1, -1)
    r, c = sr, sc
    count = 0

    while True:
        count += 1
        if grid[r][c] == 3:
            break

        nr = nc = -1
        if r > 0 and (r - 1, c) != prev and grid[r - 1][c] != 0:
            nr, nc = r - 1, c
        elif r + 1 < n and (r + 1, c) != prev and grid[r + 1][c] != 0:
            nr, nc = r + 1, c
        elif c > 0 and (r, c - 1) != prev and grid[r][c - 1] != 0:
            nr, nc = r, c - 1
        elif c + 1 < m and (r, c + 1) != prev and grid[r][c + 1] != 0:
            nr, nc = r, c + 1

        prev = (r, c)
        r, c = nr, nc

    print(count)

if __name__ == "__main__":
    main()
