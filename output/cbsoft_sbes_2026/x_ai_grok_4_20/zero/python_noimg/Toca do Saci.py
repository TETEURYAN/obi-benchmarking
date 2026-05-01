
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
count = 1  # count the starting room (with 2)

while grid[current[0]][current[1]] != 3:
    found = False
    for di, dj in directions:
        ni, nj = current[0] + di, current[1] + dj
        if 0 <= ni < N and 0 <= nj < M:
            if grid[ni][nj] == 1 or grid[ni][nj] == 3:
                # Check if this is the continuation (not previously visited in path)
                # Since path doesn't cross and is unique, we can move to next 1 or 3
                current = (ni, nj)
                count += 1
                found = True
                break
    if not found:
        # Should not happen as per problem guarantee
        break

print(count)
