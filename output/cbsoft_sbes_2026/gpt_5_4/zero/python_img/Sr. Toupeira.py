import sys

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)

S = next(it)
T = next(it)

adj = [set() for _ in range(S + 1)]
for _ in range(T):
    x = next(it)
    y = next(it)
    adj[x].add(y)
    adj[y].add(x)

P = next(it)
ans = 0

for _ in range(P):
    N = next(it)
    prev = next(it)
    ok = True
    for _ in range(N - 1):
        cur = next(it)
        if ok and cur not in adj[prev]:
            ok = False
        prev = cur
    if ok:
        ans += 1

print(ans)