import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    a = [[int(next(it)) for _ in range(n)] for _ in range(n)]

    row_sums = [sum(row) for row in a]
    col_sums = [sum(a[i][j] for i in range(n)) for j in range(n)]

    freq = {}
    for s in row_sums + col_sums:
        freq[s] = freq.get(s, 0) + 1

    M = max(freq, key=freq.get)

    bad_row = next(i for i in range(n) if row_sums[i] != M)
    bad_col = next(j for j in range(n) if col_sums[j] != M)

    changed = a[bad_row][bad_col]
    original = changed + (M - row_sums[bad_row])

    print(original, changed)

if __name__ == "__main__":
    main()