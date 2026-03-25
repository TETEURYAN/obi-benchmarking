import sys

data = sys.stdin.read().split()
if len(data) < 2:
    print("-1 -1")
    raise SystemExit

A = int(data[0])
B = int(data[1])

s = A // 2 + 2
if A % 2 != 0 or s < 2:
    print("-1 -1")
    raise SystemExit

d = s * s - 4 * B
if d < 0:
    print("-1 -1")
    raise SystemExit

r = int(d ** 0.5)
while (r + 1) * (r + 1) <= d:
    r += 1
while r * r > d:
    r -= 1

if r * r != d or (s - r) % 2 != 0:
    print("-1 -1")
    raise SystemExit

x = (s - r) // 2
y = (s + r) // 2

if x < 2 or y < 2:
    print("-1 -1")
    raise SystemExit

if 2 * x + 2 * y - 4 != A or (x - 2) * (y - 2) != B:
    print("-1 -1")
    raise SystemExit

if x > y:
    x, y = y, x
print(x, y)