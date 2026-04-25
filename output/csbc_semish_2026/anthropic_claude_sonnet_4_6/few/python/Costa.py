import sys

data = sys.stdin.read().split()
M = int(data[0])
N = int(data[1])
grid = data[2:]

count = 0
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

for i in range(M):
    for j in range(N):
        if grid[i][j] == '#':
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if ni < 0 or ni >= M or nj < 0 or nj >= N or grid[ni][nj] == '.':
                    count += 1
                    break

print(count)