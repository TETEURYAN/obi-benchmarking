
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    grid = []
    for _ in range(N):
        row = list(map(int, data[idx:idx+N]))
        grid.append(row)
        idx += N

    row_sums = [sum(row) for row in grid]
    col_sums = [0] * N
    for j in range(N):
        for i in range(N):
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
