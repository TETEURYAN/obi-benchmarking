import sys

n = int(sys.stdin.read().strip())

grid = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        grid[i][j] = min(i+1, j+1, n-i, n-j)

for i in range(n):
    print(*grid[i])