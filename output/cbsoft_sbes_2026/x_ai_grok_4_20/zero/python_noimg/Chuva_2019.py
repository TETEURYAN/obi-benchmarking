
import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0].split()[0])
M = int(data[0].split()[1])

grid = [list(line) for line in data[1:1+N]]

# Find starting point
start_col = -1
for j in range(M):
    if grid[0][j] == 'o':
        start_col = j
        break

# We will simulate the flow row by row
for i in range(N):
    # First, spread horizontally on current row where possible
    changed = True
    while changed:
        changed = False
        for j in range(1, M-1):
            if grid[i][j] != '.':
                continue
            # Check left
            if grid[i][j-1] == 'o':
                if i + 1 < N and grid[i+1][j-1] == '#':
                    grid[i][j] = 'o'
                    changed = True
                    continue
            # Check right
            if grid[i][j+1] == 'o':
                if i + 1 < N and grid[i+1][j+1] == '#':
                    grid[i][j] = 'o'
                    changed = True
                    continue
    # Now, propagate down from current row to next row
    if i + 1 < N:
        for j in range(M):
            if grid[i][j] == 'o' and grid[i+1][j] == '.':
                grid[i+1][j] = 'o'

# Output the result
for row in grid:
    print(''.join(row))
