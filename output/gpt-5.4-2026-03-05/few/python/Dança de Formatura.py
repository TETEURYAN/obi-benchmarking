import sys

data = sys.stdin.buffer.read().split()
if not data:
    sys.exit()

n = int(data[0])
m = int(data[1])
p = int(data[2])

rows = list(range(1, n + 1))
cols = list(range(1, m + 1))

idx = 3
for _ in range(p):
    op = data[idx]
    a = int(data[idx + 1]) - 1
    b = int(data[idx + 2]) - 1
    if op == b'L':
        rows[a], rows[b] = rows[b], rows[a]
    else:
        cols[a], cols[b] = cols[b], cols[a]
    idx += 3

out = []
for i in range(n):
    base = (rows[i] - 1) * m
    line = [str(base + cols[j]) for j in range(m)]
    out.append(' '.join(line))

sys.stdout.write('\n'.join(out))