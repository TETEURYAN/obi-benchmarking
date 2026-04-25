import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])

out = []
for i in range(n):
    row = []
    for j in range(n):
        v = min(i, j, n - 1 - i, n - 1 - j) + 1
        row.append(str(v))
    out.append(' '.join(row))

sys.stdout.write('\n'.join(out))