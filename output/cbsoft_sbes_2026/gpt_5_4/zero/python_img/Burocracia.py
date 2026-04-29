import sys

sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

N = int(input())
par = [0] * (N + 1)
tmp = list(map(int, input().split()))
for i in range(2, N + 1):
    par[i] = tmp[i - 2]

children = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    children[par[i]].append(i)

tin = [0] * (N + 1)
tout = [0] * (N + 1)
depth0 = [0] * (N + 1)
order = []

stack = [(1, 0)]
timer = 0
while stack:
    v, state = stack.pop()
    if state == 0:
        tin[v] = timer
        order.append(v)
        timer += 1
        stack.append((v, 1))
        for u in reversed(children[v]):
            depth0[u] = depth0[v] + 1
            stack.append((u, 0))
    else:
        tout[v] = timer - 1

Q = int(input())
ops = []
queries_by_v = [[] for _ in range(N + 1)]
restruct = [False] * (N + 1)

for idx in range(Q):
    parts = list(map(int, input().split()))
    ops.append(parts)
    if parts[0] == 1:
        _, v, k = parts
        queries_by_v[v].append((idx, k))
    else:
        _, v = parts
        restruct[v] = True

LOG = (N).bit_length()
up = [[0] * (N + 1) for _ in range(LOG)]
for v in range(1, N + 1):
    up[0][v] = par[v]
for j in range(1, LOG):
    uj = up[j]
    prev = up[j - 1]
    for v in range(1, N + 1):
        uj[v] = prev[prev[v]]

def kth_ancestor(v, k):
    b = 0
    while k:
        if k & 1:
            v = up[b][v]
        k >>= 1
        b += 1
    return v

bit = [0] * (N + 2)

def bit_add(i, delta):
    i += 1
    n = N + 1
    while i <= n:
        bit[i] += delta
        i += i & -i

def bit_sum(i):
    i += 1
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

def range_add(l, r, delta):
    bit_add(l, delta)
    if r + 1 < N:
        bit_add(r + 1, -delta)

answers = [0] * Q

stack = [(1, 0)]
while stack:
    v, state = stack.pop()
    if state == 0:
        stack.append((v, 1))
        if restruct[v]:
            range_add(tin[v], tout[v], 1)

        if queries_by_v[v]:
            cur = bit_sum(tin[v])
            for idx, k in queries_by_v[v]:
                target_depth = depth0[v] - k
                lo, hi = 0, k
                while lo < hi:
                    mid = (lo + hi) // 2
                    a = kth_ancestor(v, mid)
                    if depth0[a] + bit_sum(tin[a]) <= target_depth + cur:
                        hi = mid
                    else:
                        lo = mid + 1
                x = kth_ancestor(v, lo)
                need = target_depth + cur - bit_sum(tin[x])
                answers[idx] = kth_ancestor(x, depth0[x] - need)

        for u in reversed(children[v]):
            stack.append((u, 0))
    else:
        if restruct[v]:
            range_add(tin[v], tout[v], -1)

out = []
for i, op in enumerate(ops):
    if op[0] == 1:
        out.append(str(answers[i]))
print("\n".join(out))