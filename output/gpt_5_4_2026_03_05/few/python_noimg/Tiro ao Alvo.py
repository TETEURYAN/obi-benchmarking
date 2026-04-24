import sys
from bisect import bisect_left

data = sys.stdin.read().split()
if not data:
    sys.exit()

c = int(data[0])
t = int(data[1])

r2 = [0] * c
idx = 2
for i in range(c):
    r = int(data[idx])
    r2[i] = r * r
    idx += 1

total = 0
for _ in range(t):
    x = int(data[idx])
    y = int(data[idx + 1])
    d2 = x * x + y * y
    total += c - bisect_left(r2, d2)
    idx += 2

print(total)