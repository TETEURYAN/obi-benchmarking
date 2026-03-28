import sys

data = sys.stdin.read().split()
M = int(data[0])
N = int(data[1])
grid = data[2:]
count = 0
for i in range(M):
    for j in range(N):
        if grid[i][j] == '#':
            is_coast = False
            if i - 1 < 0 or grid[i - 1][j] == '.':
                is_coast = True
            if i + 1 >= M or grid[i + 1][j] == '.':
                is_coast = True
            if j - 1 < 0 or grid[i][j - 1] == '.':
                is_coast = True
            if j + 1 >= N or grid[i][j + 1] == '.':
                is_coast = True
            if is_coast:
                count += 1
print(count)