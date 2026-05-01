
import sys

input = sys.stdin.read
data = input().split()

M = int(data[0])
N = int(data[1])

grid = []
index = 2
for i in range(M):
    row = data[index]
    grid.append(list(row))
    index += 1

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

coast = 0
for i in range(M):
    for j in range(N):
        if grid[i][j] == '#':
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= M or nj < 0 or nj >= N:
                    coast += 1
                    break
                elif grid[ni][nj] == '.':
                    coast += 1
                    break

print(coast)
