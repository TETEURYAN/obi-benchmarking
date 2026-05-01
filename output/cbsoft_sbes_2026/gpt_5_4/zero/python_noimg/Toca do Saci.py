import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    grid = []
    idx = 2
    sr = sc = -1

    for i in range(n):
        row = data[idx:idx + m]
        idx += m
        grid.append(row)
        for j, v in enumerate(row):
            if v == 2:
                sr, sc = i, j

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    prev_r, prev_c = -1, -1
    r, c = sr, sc
    count = 1

    while grid[r][c] != 3:
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and (nr != prev_r or nc != prev_c):
                if grid[nr][nc] != 0:
                    prev_r, prev_c = r, c
                    r, c = nr, nc
                    count += 1
                    break

    print(count)

if __name__ == "__main__":
    main()
