
import sys

input = sys.stdin.read
data = input().split()

F = int(data[0])
R = int(data[1])
positions = list(map(int, data[2:]))

if R == 0:
    print(0)
    sys.exit()

max_days = 0

# From left end to first drop
max_days = max(max_days, positions[0] - 1)

# Between drops
for i in range(1, R):
    dist = positions[i] - positions[i-1] - 1
    days = (dist + 1) // 2
    max_days = max(max_days, days)

# From last drop to right end
max_days = max(max_days, F - positions[-1])

print(max_days)
