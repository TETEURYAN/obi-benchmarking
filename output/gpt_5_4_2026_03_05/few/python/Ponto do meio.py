import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
side_points = (1 << n) + 1
print(side_points * side_points)