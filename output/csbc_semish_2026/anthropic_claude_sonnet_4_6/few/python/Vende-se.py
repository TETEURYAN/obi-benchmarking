import sys

data = sys.stdin.read().split()
n = int(data[0])
k = int(data[1])
x = sorted(int(data[i+2]) for i in range(n))

remaining = n - k
min_dist = float('inf')
for i in range(n - remaining + 1):
    dist = x[i + remaining - 1] - x[i]
    if dist < min_dist:
        min_dist = dist

print(min_dist)