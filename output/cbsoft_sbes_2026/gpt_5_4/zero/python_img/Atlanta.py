import sys
import math

data = sys.stdin.read().strip().split()
A = int(data[0])
B = int(data[1])

s = A + B
d = A - 4

if d < 0 or d % 2 != 0:
    print("-1 -1")
    sys.exit()

x_plus_y = d // 2
delta = x_plus_y * x_plus_y - 4 * s

if delta < 0:
    print("-1 -1")
    sys.exit()

r = math.isqrt(delta)
if r * r != delta:
    print("-1 -1")
    sys.exit()

if (x_plus_y - r) % 2 != 0 or (x_plus_y + r) % 2 != 0:
    print("-1 -1")
    sys.exit()

x = (x_plus_y - r) // 2
y = (x_plus_y + r) // 2

if x < 2 or y < 2:
    print("-1 -1")
    sys.exit()

if x * y != s or (x - 2) * (y - 2) != B or 2 * x + 2 * y - 4 != A:
    print("-1 -1")
else:
    if x > y:
        x, y = y, x
    print(x, y)