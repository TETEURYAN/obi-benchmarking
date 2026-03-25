import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

idx = 0
M = data[idx]
N = data[idx + 1]
idx += 2

stock = [data[idx + i * N: idx + (i + 1) * N] for i in range(M)]
idx += M * N

P = data[idx]
idx += 1

sold = 0
for _ in range(P):
    i = data[idx] - 1
    j = data[idx + 1] - 1
    idx += 2
    if stock[i][j] > 0:
        stock[i][j] -= 1
        sold += 1

print(sold)