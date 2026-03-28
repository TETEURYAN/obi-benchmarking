
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    grid = []
    idx = 1
    for i in range(n):
        row = list(map(int, data[idx:idx + n]))
        grid.append(row)
        idx += n

    zero_pos = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                zero_pos = (i, j)
                break
        if zero_pos is not None:
            break

    if zero_pos is None:
        return

    i, j = zero_pos
    target_sum = sum(grid[i])

    row_sum = sum(grid[i])
    col_sum = sum(grid[k][j] for k in range(n))
    diag1_sum = sum(grid[k][k] for k in range(n))
    diag2_sum = sum(grid[k][n - 1 - k] for k in range(n))

    if i == j:
        target_sum = diag1_sum
    elif i + j == n - 1:
        target_sum = diag2_sum
    elif row_sum != col_sum:
        target_sum = row_sum if row_sum != 0 else col_sum
    else:
        target_sum = row_sum

    value = target_sum - (row_sum - 0) - (col_sum - 0) + 0

    print(value)
    print(i + 1)
    print(j + 1)

if __name__ == "__main__":
    main()
