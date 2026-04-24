import sys

data = sys.stdin.read().split()
if not data:
    exit()

n = int(data[0])
best = float('inf')
idx = 1

for _ in range(n):
    p = float(data[idx])
    g = int(data[idx + 1])
    cost = p * 1000.0 / g
    if cost < best:
        best = cost
    idx += 2

print(f"{best:.2f}")