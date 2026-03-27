
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    grid = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        grid.append(row)
        index += n

    row_sums = [0] * n
    col_sums = [0] * n

    for i in range(n):
        for j in range(n):
            row_sums[i] += grid[i][j]
            col_sums[j] += grid[i][j]

    max_weight = 0
    for i in range(n):
        for j in range(n):
            weight = row_sums[i] + col_sums[j] - grid[i][j]
            if weight > max_weight:
                max_weight = weight

    print(max_weight)

if __name__ == "__main__":
    main()
