
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

# Find position of 2
start = None
for i in range(N):
    for j in range(M):
        if grid[i][j] == 2:
            start = (i, j)
            break
    if start:
        break

# Directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Follow the path from 2 back to 3
current = start
count = 1  # count the starting room

while True:
    ci, cj = current
    if grid[ci][cj] == 3:
        break
    
    found = False
    for di, dj in directions:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < M:
            if grid[ni][nj] == 1 or grid[ni][nj] == 3:
                # Check if this is the continuation (has neighbor with 1 or 3, but we move to next 1 or 3)
                current = (ni, nj)
                count += 1
                found = True
                break
    if not found:
        # Should not happen as per problem guarantee
        break

print(count)
