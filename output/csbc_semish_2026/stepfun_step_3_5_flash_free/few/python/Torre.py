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

    row_sum = [sum(row) for row in matrix]
    col_sum = [0] * n
    for j in range(n):
        s = 0
        for i in range(n):
            s += matrix[i][j]
        col_sum[j] = s

    max_peso = 0
    for i in range(n):
        for j in range(n):
            peso = row_sum[i] + col_sum[j] - 2 * matrix[i][j]
            if peso > max_peso:
                max_peso = peso

    print(max_peso)

if __name__ == "__main__":
    main()