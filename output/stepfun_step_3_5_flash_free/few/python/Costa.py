import sys

data = sys.stdin.read().split()
if not data:
    exit()

M = int(data[0])
N = int(data[1])
grid = data[2:2+M]

count = 0
for i in range(M):
    for j in range(N):
        if grid[i][j] == '#':
            if (i-1 < 0 or grid[i-1][j] == '.') or (i+1 >= M or grid[i+1][j] == '.') or (j-1 < 0 or grid[i][j-1] == '.') or (j+1 >= N or grid[i][j+1] == '.'):
                count += 1

print(count)