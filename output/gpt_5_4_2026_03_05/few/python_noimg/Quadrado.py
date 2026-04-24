import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])

if n == 2:
    print(-1)
    sys.exit()

if n == 1:
    print(1)
    sys.exit()

base = [1, 2, 3]
for k in range(2, n):
    base.append(6 * k)

out = []
for i in range(n):
    start = 6 * i
    row = [str(x + start) for x in base]
    out.append(" ".join(row))

sys.stdout.write("\n".join(out))