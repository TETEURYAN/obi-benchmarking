import sys

data = sys.stdin.read().split()
N = int(data[0])
idx = 1
min_cost = float('inf')
for _ in range(N):
    P = float(data[idx])
    G = int(data[idx + 1])
    cost = (P * 1000) / G
    if cost < min_cost:
        min_cost = cost
    idx += 2
print(f"{min_cost:.2f}")