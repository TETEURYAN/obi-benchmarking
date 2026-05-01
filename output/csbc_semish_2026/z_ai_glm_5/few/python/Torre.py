import sys
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
    except StopIteration:
        return

    row_sums = [0] * n
    col_sums = [0] * n
    matrix = []

    for i in range(n):
        row_vals = []
        current_row_sum = 0
        for j in range(n):
            val = int(next(iterator))
            row_vals.append(val)
            current_row_sum += val
            col_sums[j] += val
        matrix.append(row_vals)
        row_sums[i] = current_row_sum

    max_weight = -1

    for i in range(n):
        for j in range(n):
            weight = row_sums[i] + col_sums[j] - 2 * matrix[i][j]
            if weight > max_weight:
                max_weight = weight

    print(max_weight)

if __name__ == '__main__':
    solve()