
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
board = []
index = 1
for i in range(N):
    row = [int(data[index + j]) for j in range(N)]
    board.append(row)
    index += N

row_sum = [0] * N
col_sum = [0] * N

for i in range(N):
    for j in range(N):
        row_sum[i] += board[i][j]
        col_sum[j] += board[i][j]

max_weight = 0
for i in range(N):
    for j in range(N):
        weight = row_sum[i] + col_sum[j] - board[i][j]
        if weight > max_weight:
            max_weight = weight

print(max_weight)
