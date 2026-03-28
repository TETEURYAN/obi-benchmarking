import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

m = data[0]
n = data[1]

balance = [0] * (n + 1)
total = 0

idx = 2
for _ in range(m):
    x = data[idx]
    v = data[idx + 1]
    y = data[idx + 2]
    idx += 3
    balance[x] -= v
    balance[y] += v
    total += v

min_total = 0
for i in range(1, n + 1):
    if balance[i] > 0:
        min_total += balance[i]

if min_total < total:
    sys.stdout.write("S\n" + str(min_total) + "\n")
else:
    sys.stdout.write("N\n" + str(min_total) + "\n")