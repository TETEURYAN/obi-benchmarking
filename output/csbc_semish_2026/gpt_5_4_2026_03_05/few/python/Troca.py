import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

it = iter(data)
n = int(next(it))
t = int(next(it))

up = [int(next(it)) for _ in range(n)]
down = [int(next(it)) for _ in range(n)]

diff = [0] * (n + 1)
for _ in range(t):
    i = int(next(it)) - 1
    j = int(next(it)) - 1
    diff[i] ^= 1
    if j + 1 < n:
        diff[j + 1] ^= 1

cur = 0
res = [0] * n
for k in range(n):
    cur ^= diff[k]
    res[k] = down[k] if cur else up[k]

print(*res)