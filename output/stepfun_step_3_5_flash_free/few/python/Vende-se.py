import sys

data = sys.stdin.read().split()
if not data:
    exit()
n = int(data[0])
k = int(data[1])
positions = list(map(int, data[2:2+n]))
positions.sort()
m = n - k
min_diff = 10**9
for i in range(n - m + 1):
    diff = positions[i+m-1] - positions[i]
    if diff < min_diff:
        min_diff = diff
print(min_diff)