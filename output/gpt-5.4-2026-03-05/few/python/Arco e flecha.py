import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
coords = data[1:]

r2 = [0] * n
prev_p = 0
idx = 0
for i in range(n):
    x = coords[idx] + prev_p
    y = coords[idx + 1] + prev_p
    idx += 2
    d = x * x + y * y
    r2[i] = d

vals = sorted(set(r2))
comp = {v: i + 1 for i, v in enumerate(vals)}

m = len(vals)
bit = [0] * (m + 1)

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

out = []
for d in r2:
    c = comp[d]
    p = sum_prefix(c)
    out.append(str(p))
    add(c, 1)

sys.stdout.write("\n".join(out))