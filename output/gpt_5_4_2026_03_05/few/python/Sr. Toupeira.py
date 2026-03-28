import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

it = iter(data)
S = int(next(it))
T = int(next(it))

adj = [0] * (S + 1)
for _ in range(T):
    x = int(next(it))
    y = int(next(it))
    adj[x] |= 1 << (y - 1)
    adj[y] |= 1 << (x - 1)

P = int(next(it))
ans = 0

for _ in range(P):
    N = int(next(it))
    prev = int(next(it))
    ok = True
    for _ in range(N - 1):
        cur = int(next(it))
        if ok and ((adj[prev] >> (cur - 1)) & 1) == 0:
            ok = False
        prev = cur
    if ok:
        ans += 1

print(ans)