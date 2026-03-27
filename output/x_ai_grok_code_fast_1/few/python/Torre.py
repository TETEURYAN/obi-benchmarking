import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
matrix = []
idx = 1
for i in range(N):
    row = [int(x) for x in input_data[idx:idx + N]]
    matrix.append(row)
    idx += N
row_sum = [0] * N
col_sum = [0] * N
for i in range(N):
    for j in range(N):
        row_sum[i] += matrix[i][j]
        col_sum[j] += matrix[i][j]
max_weight = 0
for i in range(N):
    for j in range(N):
        weight = row_sum[i] + col_sum[j] - 2 * matrix[i][j]
        if weight > max_weight:
            max_weight = weight
print(max_weight)