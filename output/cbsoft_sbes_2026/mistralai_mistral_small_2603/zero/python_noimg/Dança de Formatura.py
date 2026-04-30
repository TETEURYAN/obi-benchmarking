
import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    P = int(next(it))

    total = N * M
    row_map = list(range(1, N + 1))
    col_map = list(range(1, M + 1))

    for _ in range(P):
        op = next(it)
        a = int(next(it))
        b = int(next(it))
        if op == 'L':
            row_map[a - 1], row_map[b - 1] = row_map[b - 1], row_map[a - 1]
        else:
            col_map[a - 1], col_map[b - 1] = col_map[b - 1], col_map[a - 1]

    for i in range(N):
        for j in range(M):
            original_row = row_map[i]
            original_col = col_map[j]
            num = (original_row - 1) * M + original_col
            print(num, end=' ')
        print()

if __name__ == "__main__":
    main()
