import sys
import math

data = sys.stdin.read().split()
if len(data) < 2:
    print("-1 -1")
    exit(0)

A = int(data[0])
B = int(data[1])

if A % 2 != 0:
    print("-1 -1")
    exit(0)

soma_xy = A // 2 - 2
if soma_xy < 2:
    print("-1 -1")
    exit(0)

found = False
x = y = 0
limit = math.isqrt(B)
for d in range(1, limit + 1):
    if B % d == 0:
        other = B // d
        if d + other == soma_xy:
            x = d
            y = other
            found = True
            break

if not found:
    print("-1 -1")
else:
    W = x + 2
    H = y + 2
    if W > H:
        W, H = H, W
    print(f"{W} {H}")