import sys

sys.setrecursionlimit(200000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

it = 0
n = data[it]
it += 1

parent0 = [0] * (n + 1)
children = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    p = data[it]
    it += 1
    parent0[i] = p
    children[p].append(i)

tin = [0] * (n + 1)
tout = [0] * (n + 1)
order = [0] * (n + 1)
depth0 = [0] * (n + 1)

timer = 0
stack = [(1, 0)]
while stack:
    v, state = stack.pop()
    if state == 0:
        timer += 1
        tin[v] = timer
        order[timer] = v
        stack.append((v, 1))
        ch = children[v]
        for i in range(len(ch) - 1, -1, -1):
            u = ch[i]
            depth0[u] = depth0[v] + 1
            stack.append((u, 0))
    else:
        tout[v] = timer

LOG = (n).bit_length()
up = [[0] * (n + 1) for _ in range(LOG)]
for v in range(1, n + 1):
    up[0][v] = parent0[v]
for j in range(1, LOG):
    prev = up[j - 1]
    cur = up[j]
    for v in range(1, n + 1):
        cur[v] = prev[prev[v]]

def kth_ancestor_orig(v, k):
    b = 0
    while k:
        if k & 1:
            v = up[b][v]
        k >>= 1
        b += 1
    return v

q = data[it]
it += 1

queries = []
restructs = []
for _ in range(q):
    typ = data[it]
    it += 1
    if typ == 1:
        v = data[it]
        k = data[it + 1]
        it += 2
        queries.append((1, v, k))
    else:
        v = data[it]
        it += 1
        queries.append((2, v))
        restructs.append(v)

restructs = sorted(set(restructs), key=lambda x: tin[x])

active = []
for v in restructs:
    while active and tout[active[-1]] < tin[v]:
        active.pop()
    if active:
        pass
    active.append(v)

final_nodes = active
m = len(final_nodes)

final_parent = [0] * (n + 1)
for v in range(2, n + 1):
    final_parent[v] = parent0[v]

for v in final_nodes:
    pv = parent0[v]
    l = tin[v]
    r = tout[v]
    for pos in range(l + 1, r + 1):
        u = order[pos]
        final_parent[u] = v
    final_parent[v] = pv

children_final = [[] for _ in range(n + 1)]
for v in range(2, n + 1):
    children_final[final_parent[v]].append(v)

depthf = [0] * (n + 1)
tin2 = [0] * (n + 1)
tout2 = [0] * (n + 1)
timer = 0
stack = [(1, 0)]
while stack:
    v, state = stack.pop()
    if state == 0:
        timer += 1
        tin2[v] = timer
        stack.append((v, 1))
        ch = children_final[v]
        for i in range(len(ch) - 1, -1, -1):
            u = ch[i]
            depthf[u] = depthf[v] + 1
            stack.append((u, 0))
    else:
        tout2[v] = timer

bit = [0] * (n + 2)

def bit_add(i, delta):
    while i <= n:
        bit[i] += delta
        i += i & -i

def bit_range_add(l, r, delta):
    bit_add(l, delta)
    if r + 1 <= n:
        bit_add(r + 1, -delta)

def bit_sum(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

for v in final_nodes:
    bit_range_add(tin2[v], tout2[v], 1)

out = []

for qu in reversed(queries):
    if qu[0] == 1:
        _, v, k = qu
        cnt = bit_sum(tin2[v])
        ans = kth_ancestor_orig(v, k + cnt)
        out.append(str(ans))
    else:
        v = qu[1]
        bit_range_add(tin2[v], tout2[v], -1)

sys.stdout.write("\n".join(reversed(out)))