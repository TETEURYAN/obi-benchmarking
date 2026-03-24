import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    
    grid = []
    idx = 1
    for _ in range(n):
        grid.append([int(x) for x in input_data[idx:idx+n]])
        idx += n

    row_sums = [sum(row) for row in grid]
    col_sums = [sum(grid[i][j] for i in range(n)) for j in range(n)]

    max_weight = -1
    for i in range(n):
        r_sum = row_sums[i]
        row = grid[i]
        for j in range(n):
            w = r_sum + col_sums[j] - 2 * row[j]
            if w > max_weight:
                max_weight = w

    print(max_weight)

if __name__ == '__main__':
    main()