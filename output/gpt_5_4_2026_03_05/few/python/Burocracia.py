import sys

sys.setrecursionlimit(200000)

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

ptr = 0
n = data[ptr]
ptr += 1

parent0 = [0] * (n + 1)
children = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    p = data[ptr]
    ptr += 1
    parent0[i] = p
    children[p].append(i)

tin = [0] * (n + 1)
tout = [0] * (n + 1)
depth0 = [0] * (n + 1)
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
        ch = children[v]
        for i in range(len(ch) - 1, -1, -1):
            u = ch[i]
            depth0[u] = depth0[v] + 1
            stack.append((u, 0))
    else:
        tout[v] = timer - 1

q = data[ptr]
ptr += 1

ops = []
restruct = []
for _ in range(q):
    t = data[ptr]
    ptr += 1
    if t == 1:
        v = data[ptr]
        k = data[ptr + 1]
        ptr += 2
        ops.append((1, v, k))
    else:
        v = data[ptr]
        ptr += 1
        ops.append((2, v))
        restruct.append(v)

m = len(restruct)
if m == 0:
    LOG = (n + 1).bit_length()
    up = [[0] * (n + 1) for _ in range(LOG)]
    up[0] = parent0[:]
    for j in range(1, LOG):
        prev = up[j - 1]
        cur = up[j]
        for i in range(1, n + 1):
            cur[i] = prev[prev[i]]

    out = []
    for op in ops:
        if op[0] == 1:
            v, k = op[1], op[2]
            b = 0
            while k:
                if k & 1:
                    v = up[b][v]
                k >>= 1
                b += 1
            out.append(str(v))
    sys.stdout.write("\n".join(out))
    exit()

restruct_sorted = sorted(set(restruct), key=lambda x: tin[x])
roots = []
for v in restruct_sorted:
    if not roots or tout[roots[-1]] < tin[v]:
        roots.append(v)

root_id = [-1] * (n + 1)
root_depth = [0] * (n + 1)
for rid, r in enumerate(roots):
    d = depth0[r]
    l = tin[r]
    rr = tout[r]
    for pos in range(l, rr + 1):
        u = order[pos]
        root_id[u] = rid
        root_depth[u] = d

bit = [0] * (m + 2)

def bit_add(i, delta):
    i += 1
    while i <= m + 1:
        bit[i] += delta
        i += i & -i

def bit_sum(i):
    s = 0
    i += 1
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

events = [[] for _ in range(q + 1)]
for idx_r, v in enumerate(restruct):
    rid = root_id[v]
    if rid != -1 and roots[rid] == v:
        events[idx_r + 1].append(rid)

queries = []
for idx_op, op in enumerate(ops, 1):
    if op[0] == 1:
        v, k = op[1], op[2]
        rid = root_id[v]
        if rid == -1:
            queries.append((idx_op, v, k, -1))
        else:
            queries.append((idx_op, v, k, rid))

ans_depth = [0] * len(queries)

qi = 0
for t in range(1, q + 1):
    for rid in events[t]:
        bit_add(rid, 1)
    while qi < len(queries) and queries[qi][0] == t:
        _, v, k, rid = queries[qi]
        if rid == -1:
            ans_depth[qi] = depth0[v] - k
        else:
            cnt = bit_sum(rid)
            droot = root_depth[v]
            if k <= depth0[v] - droot:
                ans_depth[qi] = depth0[v] - k
            else:
                rem = k - (depth0[v] - droot)
                ans_depth[qi] = droot - (rem - 1) - cnt
        qi += 1

by_depth = [[] for _ in range(n + 1)]
for v in range(1, n + 1):
    by_depth[depth0[v]].append(v)

maxd = max(depth0)
for d in range(maxd + 1):
    by_depth[d].sort(key=lambda x: tin[x])

def find_descendant_at_depth(v, target_depth):
    arr = by_depth[target_depth]
    l = 0
    r = len(arr)
    tv = tin[v]
    while l < r:
        mid = (l + r) >> 1
        if tin[arr[mid]] < tv:
            l = mid + 1
        else:
            r = mid
    return arr[l]

out = []
qi = 0
for op in ops:
    if op[0] == 1:
        v = op[1]
        d = ans_depth[qi]
        out.append(str(find_descendant_at_depth(v, d)))
        qi += 1

sys.stdout.write("\n".join(out))