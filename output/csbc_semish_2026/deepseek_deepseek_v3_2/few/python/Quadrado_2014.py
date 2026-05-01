import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    grid = [[int(next(it)) for _ in range(N)] for _ in range(N)]

    row_sums = [sum(row) for row in grid]
    col_sums = [sum(grid[i][j] for i in range(N)) for j in range(N)]

    freq = {}
    for v in row_sums + col_sums:
        freq[v] = freq.get(v, 0) + 1

    M = max(freq.items(), key=lambda x: x[1])[0]

    bad_row = -1
    for i in range(N):
        if row_sums[i] != M:
            bad_row = i
            break

    bad_col = -1
    for j in range(N):
        if col_sums[j] != M:
            bad_col = j
            break

    original = M - (row_sums[bad_row] - grid[bad_row][bad_col])
    changed = grid[bad_row][bad_col]

    print(original, changed)

if __name__ == "__main__":
    main()