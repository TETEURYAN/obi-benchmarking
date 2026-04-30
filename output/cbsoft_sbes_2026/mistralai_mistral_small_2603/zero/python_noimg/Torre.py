
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    matrix = []
    for _ in range(N):
        row = list(map(int, data[idx:idx+N]))
        matrix.append(row)
        idx += N

    row_sums = [sum(row) for row in matrix]
    col_sums = [0] * N
    for j in range(N):
        s = 0
        for i in range(N):
            s += matrix[i][j]
        col_sums[j] = s

    max_weight = 0
    for i in range(N):
        for j in range(N):
            weight = row_sums[i] + col_sums[j] - matrix[i][j]
            if weight > max_weight:
                max_weight = weight
    print(max_weight)

if __name__ == "__main__":
    main()
