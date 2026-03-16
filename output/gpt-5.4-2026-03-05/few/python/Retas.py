import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, x1, x2 = data[0], data[1], data[2]

lines = []
idx = 3
for _ in range(n):
    a = data[idx]
    b = data[idx + 1]
    idx += 2
    y1 = a * x1 + b
    y2 = a * x2 + b
    lines.append((y1, y2))

lines.sort(key=lambda p: (p[0], p[1]))

ys = [p[1] for p in lines]
vals = sorted(set(ys))
comp = {v: i + 1 for i, v in enumerate(vals)}

m = len(vals)
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
processed = 0
i = 0
while i < n:
    j = i
    y1v = lines[i][0]
    while j < n and lines[j][0] == y1v:
        j += 1

    k = i
    while k < j:
        l = k
        y2v = lines[k][1]
        while l < j and lines[l][1] == y2v:
            l += 1
        cnt = l - k
        pos = comp[y2v]
        ans += cnt * (processed - sum_prefix(pos - 1))
        k = l

    k = i
    while k < j:
        l = k
        y2v = lines[k][1]
        while l < j and lines[l][1] == y2v:
            l += 1
        add(comp[y2v], l - k)
        processed += l - k
        k = l

    i = j

print(ans)