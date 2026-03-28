import sys

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, p, q = data[0], data[1], data[2]

pts = []
idx = 3
for _ in range(n):
    x = data[idx]
    y = data[idx + 1]
    idx += 2
    pts.append((x, y))

if q < 0:
    p = -p
    q = -q

pts.sort()

vals = [y * q - p * x for x, y in pts]

comp_vals = sorted(set(vals))
m = len(comp_vals)
comp = {v: i + 1 for i, v in enumerate(comp_vals)}

bit = [0] * (m + 2)

def add(i, v):
    while i <= m:
        bit[i] += v
        i += i & -i

def sum_prefix(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

ans = 0
seen = 0
for val in vals:
    pos = comp[val]
    ans += seen - sum_prefix(pos - 1)
    add(pos, 1)
    seen += 1

print(ans)