import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

E, I, V = data[0], data[1], data[2]
idx = 3

parents = [[] for _ in range(E + 1)]
children = [[] for _ in range(E + 1)]

for _ in range(I):
    a = data[idx]
    b = data[idx + 1]
    idx += 2
    children[a].append(b)
    parents[b].append(a)

initial = data[idx:idx + V]

certain = [False] * (E + 1)
for x in initial:
    certain[x] = True

changed = True
while changed:
    changed = False

    stack = [i for i in range(1, E + 1) if certain[i]]
    seen = [False] * (E + 1)
    for x in stack:
        seen[x] = True

    p = 0
    while p < len(stack):
        u = stack[p]
        p += 1
        for v in children[u]:
            if not seen[v]:
                seen[v] = True
                stack.append(v)

    for v in range(1, E + 1):
        if certain[v]:
            continue
        ps = parents[v]
        if not ps:
            continue
        ok = True
        for pnode in ps:
            if not seen[pnode]:
                ok = False
                break
        if ok:
            certain[v] = True
            changed = True

ans = [str(i) for i in range(1, E + 1) if certain[i]]
print(" ".join(ans))