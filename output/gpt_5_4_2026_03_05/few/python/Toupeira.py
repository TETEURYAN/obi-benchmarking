import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

it = iter(data)
S = int(next(it))
T = int(next(it))

adj = [set() for _ in range(S + 1)]
for _ in range(T):
    x = int(next(it))
    y = int(next(it))
    adj[x].add(y)
    adj[y].add(x)

P = int(next(it))
ans = 0

for _ in range(P):
    N = int(next(it))
    prev = int(next(it))
    ok = True
    for _ in range(N - 1):
        cur = int(next(it))
        if ok and cur not in adj[prev]:
            ok = False
        prev = cur
    if ok:
        ans += 1

print(ans)