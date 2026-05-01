
def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    grid = []
    for _ in range(N):
        row = list(map(int, input[ptr:ptr+N]))
        ptr += N
        grid.append(row)

    row_sums = [0] * N
    col_sums = [0] * N

    for i in range(N):
        for j in range(N):
            row_sums[i] += grid[i][j]
            col_sums[j] += grid[i][j]

    max_weight = 0
    for i in range(N):
        for j in range(N):
            weight = row_sums[i] + col_sums[j] - grid[i][j]
            if weight > max_weight:
                max_weight = weight

    print(max_weight)

if __name__ == "__main__":
    main()
