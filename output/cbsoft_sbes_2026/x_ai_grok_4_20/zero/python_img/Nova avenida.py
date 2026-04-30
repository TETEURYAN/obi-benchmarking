
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
    total = 0
    for row in range(N):
        total += grid[row][col]
    min_cost = min(min_cost, total)

print(min_cost)
