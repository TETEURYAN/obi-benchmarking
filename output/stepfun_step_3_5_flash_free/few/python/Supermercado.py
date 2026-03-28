import sys

data = sys.stdin.read().split()
if not data:
    exit()
n = int(data[0])
min_cost = float('inf')
idx = 1
for _ in range(n):
    p = float(data[idx])
    g = int(data[idx+1])
    idx += 2
    cost = (p * 1000) / g
    if cost < min_cost:
        min_cost = cost
print("{:.2f}".format(min_cost))