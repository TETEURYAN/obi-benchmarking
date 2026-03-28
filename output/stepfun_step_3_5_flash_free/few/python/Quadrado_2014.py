import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    matrix = []
    idx = 1
    for i in range(n):
        row = list(map(int, data[idx:idx+n]))
        matrix.append(row)
        idx += n

    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(matrix[i][j] for i in range(n)) for j in range(n)]

    M = sorted(row_sums)[n // 2]

    altered_row = next(i for i in range(n) if row_sums[i] != M)
    altered_col = next(j for j in range(n) if col_sums[j] != M)

    altered_value = matrix[altered_row][altered_col]
    original_value = M - row_sums[altered_row] + altered_value

    print(original_value, altered_value)

if __name__ == "__main__":
    main()