
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

grid = []
index = 2
for i in range(N):
    row = []
    for j in range(M):
        row.append(int(data[index]))
        index += 1
    grid.append(row)

min_cost = float('inf')

for col in range(M):
    left_sum = 0
    right_sum = 0
    for row in range(N):
        if col > 0:
            left_sum += grid[row][col - 1]
        if col < M - 1:
            right_sum += grid[row][col + 1]
    cost = left_sum + right_sum
    if cost < min_cost:
        min_cost = cost

print(min_cost)
