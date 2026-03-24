import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

m = int(data[0])
n = int(data[1])
grid = data[2:2 + m]

ans = 0
for i in range(m):
    row = grid[i]
    for j in range(n):
        if row[j] == '#':
            coast = False
            if i == 0 or grid[i - 1][j] == '.':
                coast = True
            elif i == m - 1 or grid[i + 1][j] == '.':
                coast = True
            elif j == 0 or row[j - 1] == '.':
                coast = True
            elif j == n - 1 or row[j + 1] == '.':
                coast = True
            if coast:
                ans += 1

print(ans)