import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, x1, x2 = data[0], data[1], data[2]

lines = []
idx = 3
for i in range(n):
    a = data[idx]
    b = data[idx + 1]
    idx += 2
    y1 = a * x1 + b
    y2 = a * x2 + b
    lines.append((y1, y2, i))

lines.sort(key=lambda t: (t[0], t[1], t[2]))

arr = [t[1] for t in lines]

vals = sorted(set(arr))
comp = {v: i + 1 for i, v in enumerate(vals)}

size = len(vals)
bit = [0] * (size + 2)

def add(i, v):
    while i <= size:
        bit[i] += v
        i += i & -i

def sum_prefix(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

ans = 0
processed = 0
for v in arr:
    p = comp[v]
    leq = sum_prefix(p)
    ans += processed - leq
    add(p, 1)
    processed += 1

print(ans)