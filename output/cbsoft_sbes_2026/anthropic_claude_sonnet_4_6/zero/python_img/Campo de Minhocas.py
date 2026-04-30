n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

max_sum = 0

for i in range(n):
    s = sum(grid[i])
    if s > max_sum:
        max_sum = s

for j in range(m):
    s = sum(grid[i][j] for i in range(n))
    if s > max_sum:
        max_sum = s

print(max_sum)