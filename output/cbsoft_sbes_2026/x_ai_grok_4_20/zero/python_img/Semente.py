
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
first = positions[0]
days_left = first - 1
max_days = max(max_days, days_left)

# Between drops
for i in range(1, R):
    dist = positions[i] - positions[i-1] - 1
    days_between = (dist + 1) // 2
    max_days = max(max_days, days_between)

# From last drop to right end
last = positions[-1]
days_right = F - last
max_days = max(max_days, days_right)

print(max_days)
