import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
next_piece = {}
idx = 1

for _ in range(n):
    e = int(data[idx])
    c = data[idx + 1]
    d = int(data[idx + 2])
    next_piece[e] = (c, d)
    idx += 3

res = []
cur = 0
for _ in range(n):
    c, cur = next_piece[cur]
    res.append(c)

sys.stdout.write(''.join(res) + '\n')