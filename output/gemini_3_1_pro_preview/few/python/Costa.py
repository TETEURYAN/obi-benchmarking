import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

m = int(input_data[0])
n = int(input_data[1])
grid = input_data[2:]

coast_count = 0

for i in range(m):
    row = grid[i]
    row_above = grid[i-1] if i > 0 else None
    row_below = grid[i+1] if i < m - 1 else None
    
    for j in range(n):
        if row[j] == '#':
            if row_above is None or row_above[j] == '.' or \
               row_below is None or row_below[j] == '.' or \
               j == 0 or row[j-1] == '.' or \
               j == n - 1 or row[j+1] == '.':
                coast_count += 1

print(coast_count)